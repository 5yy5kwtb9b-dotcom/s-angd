#!/usr/bin/env python3
"""用一次用户消息在全新 Codex 对话中回归 REA 总清单。"""
import argparse
import hashlib
import json
import os
from pathlib import Path
import queue
import re
import shutil
import signal
import subprocess
import sys
import tempfile
import threading
import time
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime

HERE = Path(__file__).resolve().parent
SOURCE = HERE.parent
GUIDE = "123条零报错指令中文总清单.md"
HISTORY = "123条总清单逐条验收.json"
FIXTURES = "测试样例.zip"
FILES = (GUIDE, FIXTURES, "Codex对话可用工具中文清单.md")
ZIP_SHA = "d5f4f569f5641e2d5b202a4e67db77025e1907ac60864a683bccecfe7d67941b"
ALL = set(range(1, 124))
MISSING = object()
STOP = threading.Event()


def sha(data):
    return hashlib.sha256(data).hexdigest()


def load_cases():
    cases = {}
    baseline = json.loads((SOURCE / HISTORY).read_text(encoding="utf-8"))["逐条结果"]
    headings = re.split(r"^### (\d+) · `(\w+)`[ \t]*$", (SOURCE / GUIDE).read_bytes().decode(), flags=re.M)
    for number, name, section in zip(headings[1::3], headings[2::3], headings[3::3]):
        prompts = re.findall(r"^```text\n(.*?)\n```[ \t]*$", section, re.M | re.S)
        number = int(number)
        if number in cases or len(prompts) != 1:
            raise ValueError(f"总清单第 {number} 条重复或缺少唯一文本框")
        cases[number] = dict(id=number, tool=name, prompt=prompts[0], checks=[])
    if set(cases) != ALL or len(baseline) != 123 or {r["编号"] for r in baseline} != ALL:
        raise ValueError("总清单和验收记录均须完整覆盖 1–123")
    for row in baseline:
        case = cases[row["编号"]]
        digest = sha(case["prompt"].encode())
        accepted = row["验收记录"][-1]
        if (row["工具"] != case["tool"] or row["最终指令"] != case["prompt"]
                or accepted["指令SHA256"] != digest or not accepted["完成目标"] or accepted["MCP报错次数"]):
            raise ValueError(f"清单与最终验收基线不一致，编号 {case['id']}")
        case.update(sha256=digest, reference=row["本轮最终实测结果"],
                    server="mac_pcap" if case["id"] <= 3 else "rea")
    for line in (HERE / "checks.tsv").read_text(encoding="utf-8").splitlines():
        if not line or line.startswith("#"):
            continue
        number, path, op, value = line.split("\t")
        if op not in {"eq", "contains", "length", "nonempty", "positive", "list"}:
            raise ValueError(f"未知断言 {op}")
        cases[int(number)]["checks"].append((path, op, json.loads(value)))
    if not all(case["checks"] for case in cases.values()):
        raise ValueError("每个编号都必须有实际返回值断言")
    if sha((SOURCE / FIXTURES).read_bytes()) != ZIP_SHA or not all((SOURCE / n).is_file() for n in FILES):
        raise ValueError("样例包指纹不符或缺少准备文件")
    return cases


def select_ids(expr):
    selected = set()
    for part in expr.split(","):
        m = re.fullmatch(r"(\d+)(?:-(\d+))?", part.strip())
        if not m:
            raise ValueError(f"无效编号 {part!r}")
        first, last = int(m[1]), int(m[2] or m[1])
        if not 1 <= first <= last <= 123:
            raise ValueError(f"无效范围 {part!r}")
        selected.update(range(first, last + 1))
    return sorted(selected)


def has_text(value, expected):
    if isinstance(value, dict):
        return any(has_text(v, expected) for v in value.values())
    if isinstance(value, list):
        return any(has_text(v, expected) for v in value)
    return isinstance(value, str) and expected in value


def matches(payload, rule):
    path, op, expected = rule
    return any(match_path(payload, part, op, expected) for part in path.split("|"))


def match_path(payload, path, op, expected):
    value = payload
    for part in ([] if path == "." else path.split(".")):
        if isinstance(value, dict) and part in value:
            value = value[part]
        elif isinstance(value, list) and part.isdigit() and int(part) < len(value):
            value = value[int(part)]
        else:
            return False
    if op == "eq":
        return type(value) is type(expected) and value == expected
    if op == "contains":
        return has_text(value, expected)
    if op == "length":
        return isinstance(value, list) and len(value) == expected
    if op == "nonempty":
        return isinstance(value, (list, str, dict)) and bool(value)
    if op == "positive":
        return type(value) in (int, float) and value > 0
    return isinstance(value, list)


def mcp_result(item):
    result = item.get("result") or {}
    body = result.get("structuredContent", result.get("structured_content", MISSING))
    if body is MISSING:
        for block in result.get("content", []):
            if block.get("type") == "text" and block.get("text"):
                try:
                    body = json.loads(block["text"])
                except ValueError:
                    body = block["text"]
                break
    err = item.get("error")
    if isinstance(body, dict) and ("error" in body or body.get("ok") is False):
        err = body.get("error") or "工具返回 ok=false"
    if item.get("status") != "completed" or result.get("isError") or body is MISSING or err is not None:
        return MISSING, err or f"MCP {item.get('status')}，错误标记或缺少结果"
    if isinstance(body, dict):
        return body.get("normalized_result", body.get("result", body)), None
    return body, None


class AppServer:
    def __init__(self, cwd, log):
        self.cwd = cwd
        self.process = subprocess.Popen(["codex", "app-server", "--stdio"], cwd=cwd,
            stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=log, text=True,
            encoding="utf-8", start_new_session=True)
        self.events = queue.Queue()
        self.sequence = 0
        threading.Thread(target=self.read, daemon=True).start()

    def read(self):
        try:
            for line in self.process.stdout:
                self.events.put(json.loads(line))
        except (ValueError, OSError) as err:
            self.events.put({"reader_error": str(err)})
        finally:
            self.events.put(None)

    def send(self, message):
        self.process.stdin.write(json.dumps(message) + "\n")
        self.process.stdin.flush()

    def next_event(self, deadline):
        while not STOP.is_set():
            remaining = deadline - time.monotonic()
            if remaining <= 0:
                raise TimeoutError("等待 Codex 响应超时")
            try:
                event = self.events.get(timeout=min(1, remaining))
                break
            except queue.Empty:
                continue
        else:
            raise InterruptedError("用户中断了本轮回归")
        if event is None or "reader_error" in event:
            raise RuntimeError(f"app-server 输出中断，详见 server.log：{event}")
        if "method" in event and "id" in event:
            raise RuntimeError(f"需要交互，结束本例：{event['method']}")
        return event

    def rpc(self, method, params, pending):
        self.sequence += 1
        self.send(dict(id=self.sequence, method=method, params=params))
        deadline = time.monotonic() + 135
        while True:
            event = self.next_event(deadline)
            if event.get("id") == self.sequence and "method" not in event:
                if "error" in event:
                    raise RuntimeError(f"{method}：{event['error']}")
                return event["result"]
            # A fast item notification can arrive before the turn/start reply.
            if event.get("method") in ("item/started", "item/completed", "turn/completed"):
                pending.append(event)

    def run(self, case, report, timeout):
        pending = []
        self.rpc("initialize", {"clientInfo": {"name": "rea-regression", "version": "1"},
                                "capabilities": {"experimentalApi": True}}, pending)
        self.send({"method": "initialized"})
        params = dict(cwd=str(self.cwd), ephemeral=True, approvalPolicy="on-request",
                      approvalsReviewer="auto_review", sandbox="workspace-write")
        thread = self.rpc("thread/start", params, pending)["thread"]["id"]
        report["thread"] = thread
        # Exactly one turn/start. No preflight messages, follow-ups or in-chat retries.
        turn = self.rpc("turn/start", {"threadId": thread, "effort": "low",
                        "input": [{"type": "text", "text": case["prompt"]}]}, pending)["turn"]["id"]
        report["turn"] = turn
        active_calls = set()
        deadline = time.monotonic() + timeout
        while True:
            event = pending.pop(0) if pending else self.next_event(deadline)
            params = event.get("params") or {}
            if params.get("threadId") != thread:
                continue
            if params.get("turnId") == turn:
                item = params.get("item") or {}
                if event.get("method") == "item/started" and item.get("type") == "mcpToolCall":
                    active_calls.add(item["id"])
                if event.get("method") == "item/completed":
                    active_calls.discard(item["id"])
                    record_item(item, case, report)
            if event.get("method") == "turn/completed" and params["turn"]["id"] == turn:
                report["turn_status"] = params["turn"]["status"]
                if active_calls:
                    report["error"] = "轮次结束时仍有未返回的 MCP 调用"
                if params["turn"].get("error"):
                    report["error"] = params["turn"]["error"]
                return

    def close(self):
        # Only the process group started for this case is signalled.
        try:
            os.killpg(self.process.pid, signal.SIGTERM)
            self.process.wait(timeout=5)
        except subprocess.TimeoutExpired:
            os.killpg(self.process.pid, signal.SIGKILL)
            self.process.wait()
        except ProcessLookupError:
            self.process.wait()
        self.process.stdin.close()
        self.process.stdout.close()


def record_item(item, case, report):
    kind = item.get("type")
    if kind == "userMessage":
        parts = item.get("content", [])
        exact = len(parts) == 1 and parts[0].get("type") == "text" and parts[0].get("text") == case["prompt"]
        report["messages_match"].append(exact)
    elif kind == "agentMessage" and item.get("phase") == "final_answer":
        report["answer"] = item.get("text", "")
    elif kind == "mcpToolCall":
        payload, error = mcp_result(item)
        call = {"server": item.get("server"), "tool": item.get("tool"), "ok": error is None}
        if error is not None:
            call["error"] = error
        report["calls"].append(call)
        if (call["server"], call["tool"]) == (case["server"], case["tool"]) and error is None:
            report.setdefault("_target_results", []).append(payload)
            for check in report["checks"]:
                if matches(payload, check["rule"]):
                    check["matched"] = True


def save(path, value):
    temp = path.with_suffix(".tmp")
    temp.write_text(json.dumps(value, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    temp.replace(path)


def run_case(case, directory, timeout):
    folder = directory / f"{case['id']:03}"
    work = folder / "s-angd"
    report = {k: case[k] for k in ("id", "server", "tool", "prompt", "sha256", "reference")}
    report.update(calls=[], messages_match=[], answer="", checks=[
        {"rule": rule, "matched": False} for rule in case["checks"]])
    try:
        if STOP.is_set():
            return None
        dest = work / "tools" / "rea"
        dest.mkdir(parents=True)
        for n in FILES:
            shutil.copyfile(SOURCE / n, dest / n)
        with (folder / "server.log").open("w", encoding="utf-8") as log:
            server = AppServer(work, log)
            try:
                server.run(case, report, timeout)
            finally:
                server.close()
    except (OSError, RuntimeError, ValueError, KeyError) as err:
        report["error"] = str(err)
    report["passed"] = (not report.get("error") and report.get("turn_status") == "completed"
                        and report["messages_match"] == [True] and bool(report["answer"].strip())
                        and all(c["ok"] for c in report["calls"])
                        and all(c["matched"] for c in report["checks"]))
    payloads = report.pop("_target_results", [])
    if not report["passed"] and payloads:
        save(folder / "target-results.json", payloads)
    save(folder / "result.json", report)
    print(f"{case['id']:03} {'PASS' if report['passed'] else 'FAIL'} {case['tool']}", flush=True)
    return report


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--ids", default="1-123", help="例如 1,5,54-58，默认全量")
    parser.add_argument("--list", action="store_true", help="只校验基线并列出用例")
    parser.add_argument("--jobs", type=int, default=1, help="并行的独立对话数，默认 1")
    parser.add_argument("--timeout", type=int, default=900, help="每轮等待上限（秒）")
    parser.add_argument("--output", type=Path, help="报告父目录，每次运行都会创建新的子目录")
    args = parser.parse_args()
    try:
        cases = load_cases()
        selected = select_ids(args.ids)
        if args.jobs < 1 or args.timeout < 1:
            raise ValueError("--jobs 和 --timeout 必须是正整数")
        if args.list:
            for i in selected:
                print(i, cases[i]["server"], cases[i]["tool"], cases[i]["sha256"])
            return 0
        if not shutil.which("codex"):
            raise ValueError("PATH 中未找到 codex")
        if args.output:
            args.output.mkdir(parents=True, exist_ok=True)
        directory = Path(tempfile.mkdtemp(prefix="rea-" + datetime.now().strftime("%Y%m%d-%H%M%S-"),
                                          dir=args.output)).resolve()
    except (OSError, ValueError, KeyError) as err:
        parser.error(str(err))
    print(f"报告目录：{directory}", flush=True)
    save(directory / "plan.json", {"selected": selected, "fixture_sha256": ZIP_SHA,
         "runner_sha256": sha(Path(__file__).read_bytes()),
         "guide_sha256": sha((SOURCE / GUIDE).read_bytes()), "checks_sha256": sha((HERE / "checks.tsv").read_bytes())})
    pool = ThreadPoolExecutor(max_workers=args.jobs)
    futures = []
    interrupted = False
    try:
        for i in selected:
            futures.append(pool.submit(run_case, cases[i], directory, args.timeout))
        for future in futures:
            future.result()
    except KeyboardInterrupt:
        interrupted = True
        STOP.set()
    finally:
        pool.shutdown(wait=True, cancel_futures=interrupted)
    results = [json.loads(path.read_text(encoding="utf-8"))
               for path in sorted(directory.glob("[0-9][0-9][0-9]/result.json"))]
    threads = [r["thread"] for r in results if r.get("thread")]
    failed = [r["id"] for r in results if not r["passed"]]
    unique = len(threads) == len(set(threads))
    save(directory / "summary.json", {"planned": len(selected), "completed_cases": len(results), "interrupted": interrupted,
         "missing_ids": sorted(set(selected) - {r["id"] for r in results}),
         "passed": len(results) - len(failed), "failed_ids": failed, "unique_threads": unique,
         "mcp_calls": sum(len(r["calls"]) for r in results),
         "mcp_errors": sum(not c["ok"] for r in results for c in r["calls"])})
    print(f"用例通过 {len(results)-len(failed)}/{len(selected)}，失败编号 {failed}，对话 ID 唯一 {unique}")
    return 130 if interrupted else int(bool(failed) or not unique or len(results) != len(selected))


if __name__ == "__main__":
    sys.exit(main())
