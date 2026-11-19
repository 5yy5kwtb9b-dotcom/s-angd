const { spawnSync } = require("node:child_process");
const fs = require("node:fs");
const path = require("node:path");
const { createRequire } = require("node:module");

// Use the same installed MCP SDK as the local REA service.
const localRequire = createRequire(path.join(process.env.REA_PACKAGE_DIR, "package.json"));
const { McpServer } = localRequire("@modelcontextprotocol/server");
const { serveStdio } = localRequire("@modelcontextprotocol/server/stdio");
const { z } = localRequire("zod/v4");
const bin = process.env.WIRESHARK_BIN_DIR;
const captureMagic = new Set(["d4c3b2a1", "a1b2c3d4", "4d3cb2a1", "a1b23c4d", "0a0d0d0a"]);
const capturePath = z.string().describe("Absolute path to a local uncompressed pcap or pcapng, up to 32 MiB.");
const fieldName = z.string().max(160).regex(/^[A-Za-z0-9_][A-Za-z0-9_.-]*$/);

function run(program, args, input) {
  const result = spawnSync(path.join(bin, program), args, {
    stdio: [input ?? "ignore", "pipe", "pipe"],
    encoding: "utf8", timeout: 15000, killSignal: "SIGKILL", maxBuffer: 2 * 1024 * 1024,
    env: { ...process.env, LC_ALL: "C", TZ: "UTC" }
  });
  if (result.error) throw new Error(`${program}: ${result.error.message}. Try a narrower query or a smaller capture.`);
  if (result.status !== 0) throw new Error(result.stderr.trim().slice(0, 800) || `${program} stopped (${result.signal || result.status}).`);
  return result.stdout;
}

function withCapture(file, analyze) {
  if (!path.isAbsolute(file)) throw new Error("Use an absolute capture file path.");
  const descriptor = fs.openSync(file, fs.constants.O_RDONLY | fs.constants.O_NONBLOCK);
  try {
    const stat = fs.fstatSync(descriptor);
    if (!stat.isFile() || stat.size > 32 * 1024 * 1024) throw new Error("Choose a regular capture file up to 32 MiB.");
    const magic = Buffer.alloc(4);
    fs.readSync(descriptor, magic, 0, 4, 0);
    if (!captureMagic.has(magic.toString("hex"))) throw new Error("Expected uncompressed pcap or pcapng content.");
    return analyze(descriptor);
  } finally {
    fs.closeSync(descriptor);
  }
}

const server = new McpServer({ name: "mac_pcap", version: "1.0.0" });
function register(name, description, shape, handler) {
  server.registerTool(name, {
    description, inputSchema: z.strictObject(shape),
    annotations: { readOnlyHint: true, destructiveHint: false, idempotentHint: true, openWorldHint: false }
  }, (input) => {
    try {
      const data = handler(input);
      return { structuredContent: data, content: [{ type: "text", text: JSON.stringify(data) }] };
    } catch (error) {
      return { isError: true, content: [{ type: "text", text: error.message }] };
    }
  });
}

register("inspect_packet_fields", "Find Wireshark field names and labels by abbreviation prefix, for example frame.len or udp.", {
  query: fieldName, limit: z.int().min(1).max(100).default(25)
}, ({ query, limit }) => {
  const output = run("tshark", ["-G", "fields," + query]);
  const matches = output.split("\n").filter(line => line.includes("\t"));
  const fields = matches.slice(0, limit).map(line => {
    const [name, label] = line.split("\t");
    return { name, label };
  });
  return { fields, total_matches: matches.length };
});

register("inspect_packet_capture", "Read chosen fields from saved packets. packet_limit counts input frames before the optional Wireshark display filter. Repeated values use a comma.", {
  path: capturePath, fields: z.array(fieldName).min(1).max(16),
  packet_limit: z.int().min(1).max(500).default(50),
  display_filter: z.string().min(1).max(512).optional()
}, ({ path: file, fields, packet_limit, display_filter }) => withCapture(file, fd => {
  const args = ["-n", "-r", "-", "-c", String(packet_limit), "-T", "fields", "-E", "escape=y"];
  if (display_filter) args.push("-Y", display_filter);
  for (const field of fields) args.push("-e", field);
  const output = run("tshark", args, fd);
  const rows = output ? output.replace(/\n$/, "").split("\n").map(line => line.split("\t")) : [];
  return { fields, rows, input_packet_limit: packet_limit };
}));

register("inspect_pcap_capture", "Summarize a saved capture with capinfos: file format, encapsulation, packet count, capture bytes, wire bytes and duration.", {
  path: capturePath
}, ({ path: file }) => withCapture(file, fd => {
  const output = run("capinfos", ["-T", "-B", "-N", "-t", "-E", "-c", "-s", "-d", "-u", "-"], fd);
  const [, row] = output.trimEnd().split("\n");
  const [, format, encapsulation, count, size, data, duration] = row.split("\t");
  const number = value => value && Number.isFinite(Number(value)) ? Number(value) : null;
  return { format, encapsulation, packet_count: number(count), file_bytes: number(size),
    wire_bytes: number(data), duration_seconds: number(duration) };
}));

serveStdio(() => server);
