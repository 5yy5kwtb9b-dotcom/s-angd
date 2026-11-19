# 第 66 条修订后的全量回归 · 2026-11-20

本轮在同一台 Mac 上运行第 66 条单测通过后的仓库版本。每个编号只执行一次，最多 5 个独立对话并行。

**首轮通过 119/123，MCP 报错 2 次。** 共记录 225 次 MCP 调用，命中 135/139 条断言。核对得到 123 个不同的对话 ID、123 个不同的轮次 ID，123 条仅发送一次清单原文。

第 66 条 `set_address_name` 本轮未通过，改名断言命中 0/1，MCP 报错 2 次。

旧记录显示改名成功、关闭失败，对话答复报告快照未能保存。用仓库样例在独立 REA 进程对照复现，改名后带 snapshot_path 关闭会因不可变分析快照已失效而返回 evidence_integrity_mismatch；同一会话改用空参数关闭成功。旧记录未保存实际关闭参数。

[复现诊断与单条对话记录（5 次调用）](./single-066.json) · [第 66 条最终原文](https://github.com/5yy5kwtb9b-dotcom/s-angd/blob/aef6546ab3764d6a59c73d66defd87bf6fa8562c/tools/rea/123条零报错指令中文总清单.md#item-66)

[脚本及逐条断言](https://github.com/5yy5kwtb9b-dotcom/s-angd/blob/aef6546ab3764d6a59c73d66defd87bf6fa8562c/tools/rea/regression) · [运行计划与汇总](./summary.json) · [逐条调用、断言和最终答复](./results.json)

## 首轮失败项

- [第 66 条 `set_address_name`](./results.json#L2809)　自动审批服务对 set_address_name 和空参数 close_binary 都返回 HTTP 403。两次操作均未执行；同地址回读仍为原名 _demo_value。
- [第 73 条 `inspect_pe_resources`](./results.json#L3130)　Codex 工作区路由发现超时，轮次失败，尚未调用目标工具。
- [第 86 条 `inspect_managed_artifact`](./results.json#L3610)　目标工具成功返回，在 summary.assembly.name 读到 Fixture.Managed。现有断言仅核对 assembly.name，因此判为失败；本条 MCP 零报错。
- [第 98 条 `inspect_desktop_application`](./results.json#L4138)　目标工具成功返回，在 summary.candidates 读到空列表。现有断言仅核对 candidates，因此判为失败；本条 MCP 零报错。

## 逐条结果

编号链接指向本轮机器记录。每条的最终答复已处理本机路径。审批服务的 HTML 错误页仅保留状态码、审批结果及操作是否执行。JSON 同时保留实际调用、消息核对、各项断言和原始结果文件的指纹。编号 1–3 使用 Mac 替代工具。

| 编号 | 目标工具 | 首轮 | 原文消息数 | MCP 调用 | MCP 报错 | 命中断言 |
|---:|---|---|---:|---:|---:|---:|
| [1](./results.json#L3) | `inspect_packet_fields` | 通过 | 1 | 1 | 0 | 1/1 |
| [2](./results.json#L40) | `inspect_packet_capture` | 通过 | 1 | 1 | 0 | 1/1 |
| [3](./results.json#L86) | `inspect_pcap_capture` | 通过 | 1 | 1 | 0 | 2/2 |
| [4](./results.json#L131) | `inspect_pcap_client` | 通过 | 1 | 1 | 0 | 2/2 |
| [5](./results.json#L176) | `inspect_web_network_capture` | 通过 | 1 | 1 | 0 | 3/3 |
| [6](./results.json#L229) | `inspect_web_page` | 通过 | 1 | 1 | 0 | 1/1 |
| [7](./results.json#L266) | `inspect_web_event_listeners` | 通过 | 1 | 1 | 0 | 1/1 |
| [8](./results.json#L303) | `capture_web_screenshot` | 通过 | 1 | 1 | 0 | 1/1 |
| [9](./results.json#L340) | `compare_web_screenshots` | 通过 | 1 | 2 | 0 | 1/1 |
| [10](./results.json#L382) | `observe_web_session` | 通过 | 1 | 1 | 0 | 1/1 |
| [11](./results.json#L419) | `compare_web_captures` | 通过 | 1 | 1 | 0 | 1/1 |
| [12](./results.json#L456) | `discover_webmcp_tools` | 通过 | 1 | 1 | 0 | 1/1 |
| [13](./results.json#L493) | `inspect_playwright_trace` | 通过 | 1 | 1 | 0 | 1/1 |
| [14](./results.json#L530) | `inspect_electron_page` | 通过 | 1 | 1 | 0 | 1/1 |
| [15](./results.json#L567) | `inspect_electron_fuses` | 通过 | 1 | 1 | 0 | 1/1 |
| [16](./results.json#L604) | `analyze_javascript_application` | 通过 | 1 | 1 | 0 | 1/1 |
| [17](./results.json#L641) | `trace_application_feature` | 通过 | 1 | 2 | 0 | 1/1 |
| [18](./results.json#L683) | `trace_javascript_semantics` | 通过 | 1 | 2 | 0 | 1/1 |
| [19](./results.json#L725) | `trace_web_module_imports` | 通过 | 1 | 1 | 0 | 1/1 |
| [20](./results.json#L762) | `trace_web_source_location` | 通过 | 1 | 1 | 0 | 1/1 |
| [21](./results.json#L799) | `export_web_scripts` | 通过 | 1 | 1 | 0 | 1/1 |
| [22](./results.json#L836) | `compare_source_to_bundle` | 通过 | 1 | 2 | 0 | 1/1 |
| [23](./results.json#L878) | `compare_application_versions` | 通过 | 1 | 4 | 0 | 2/2 |
| [24](./results.json#L938) | `compare_javascript_export_shapes` | 通过 | 1 | 3 | 0 | 1/1 |
| [25](./results.json#L985) | `observe_javascript_runtime` | 通过 | 1 | 1 | 0 | 1/1 |
| [26](./results.json#L1022) | `reconcile_javascript_runtime` | 通过 | 1 | 3 | 0 | 1/1 |
| [27](./results.json#L1069) | `compare_static_and_observed_endpoints` | 通过 | 1 | 3 | 0 | 1/1 |
| [28](./results.json#L1116) | `inspect_api_contract` | 通过 | 1 | 1 | 0 | 1/1 |
| [29](./results.json#L1153) | `inspect_android_package` | 通过 | 1 | 1 | 0 | 1/1 |
| [30](./results.json#L1190) | `inspect_apk_signature` | 通过 | 1 | 1 | 0 | 1/1 |
| [31](./results.json#L1227) | `search_android_classes` | 通过 | 1 | 1 | 0 | 1/1 |
| [32](./results.json#L1264) | `inspect_android_class` | 通过 | 1 | 1 | 0 | 1/1 |
| [33](./results.json#L1301) | `inspect_apktool_client` | 通过 | 1 | 1 | 0 | 1/1 |
| [34](./results.json#L1338) | `decode_android_resources` | 通过 | 1 | 2 | 0 | 2/2 |
| [35](./results.json#L1388) | `inspect_adb_client` | 通过 | 1 | 1 | 0 | 1/1 |
| [36](./results.json#L1425) | `list_adb_devices` | 通过 | 1 | 1 | 0 | 1/1 |
| [37](./results.json#L1462) | `project_android_application_graph` | 通过 | 1 | 4 | 0 | 1/1 |
| [38](./results.json#L1514) | `identify_flutter_build` | 通过 | 1 | 1 | 0 | 1/1 |
| [39](./results.json#L1551) | `inspect_dart_aot` | 通过 | 1 | 1 | 0 | 1/1 |
| [40](./results.json#L1588) | `project_harmony_application_graph` | 通过 | 1 | 4 | 0 | 1/1 |
| [41](./results.json#L1640) | `project_apple_application_graph` | 通过 | 1 | 4 | 0 | 1/1 |
| [42](./results.json#L1692) | `open_bundle_resources` | 通过 | 1 | 1 | 0 | 1/1 |
| [43](./results.json#L1729) | `decode_interface_builder` | 通过 | 1 | 2 | 0 | 1/1 |
| [44](./results.json#L1771) | `inspect_asset_catalog` | 通过 | 1 | 3 | 0 | 1/1 |
| [45](./results.json#L1818) | `inspect_keyed_archive` | 通过 | 1 | 2 | 0 | 1/1 |
| [46](./results.json#L1860) | `inspect_plist` | 通过 | 1 | 2 | 0 | 1/1 |
| [47](./results.json#L1902) | `inspect_macho` | 通过 | 1 | 3 | 0 | 2/2 |
| [48](./results.json#L1957) | `inspect_signature` | 通过 | 1 | 3 | 0 | 1/1 |
| [49](./results.json#L2004) | `inspect_apple_ips` | 通过 | 1 | 1 | 0 | 1/1 |
| [50](./results.json#L2041) | `demangle_swift` | 通过 | 1 | 2 | 0 | 1/1 |
| [51](./results.json#L2083) | `analyze_swift_types` | 通过 | 1 | 2 | 0 | 1/1 |
| [52](./results.json#L2125) | `get_objc_classes` | 通过 | 1 | 2 | 0 | 1/1 |
| [53](./results.json#L2167) | `get_objc_protocols` | 通过 | 1 | 3 | 0 | 1/1 |
| [54](./results.json#L2214) | `open_binary` | 通过 | 1 | 2 | 0 | 1/1 |
| [55](./results.json#L2256) | `binary_session` | 通过 | 1 | 1 | 0 | 1/1 |
| [56](./results.json#L2293) | `close_binary` | 通过 | 1 | 5 | 0 | 1/1 |
| [57](./results.json#L2350) | `binary_overview` | 通过 | 1 | 3 | 0 | 2/2 |
| [58](./results.json#L2405) | `list_architectures` | 通过 | 1 | 3 | 0 | 2/2 |
| [59](./results.json#L2460) | `list_documents` | 通过 | 1 | 3 | 0 | 1/1 |
| [60](./results.json#L2507) | `list_segments` | 通过 | 1 | 4 | 0 | 1/1 |
| [61](./results.json#L2559) | `list_procedures` | 通过 | 1 | 3 | 0 | 1/1 |
| [62](./results.json#L2606) | `search_procedures` | 通过 | 1 | 4 | 0 | 1/1 |
| [63](./results.json#L2658) | `list_names` | 通过 | 1 | 3 | 0 | 1/1 |
| [64](./results.json#L2705) | `address_name` | 通过 | 1 | 4 | 0 | 1/1 |
| [65](./results.json#L2757) | `inspect_address_context` | 通过 | 1 | 4 | 0 | 1/1 |
| [66](./results.json#L2809) | `set_address_name` | 失败 | 1 | 5 | 2 | 0/1 |
| [67](./results.json#L2877) | `set_addresses_names` | 通过 | 1 | 4 | 0 | 2/2 |
| [68](./results.json#L2937) | `list_cutter_sessions` | 通过 | 1 | 1 | 0 | 1/1 |
| [69](./results.json#L2974) | `inspect_native_exports` | 通过 | 1 | 1 | 0 | 1/1 |
| [70](./results.json#L3011) | `inspect_binary_hardening` | 通过 | 1 | 1 | 0 | 1/1 |
| [71](./results.json#L3048) | `inspect_byte_entropy` | 通过 | 1 | 1 | 0 | 1/1 |
| [72](./results.json#L3085) | `inspect_pe_imports` | 通过 | 1 | 1 | 0 | 2/2 |
| [73](./results.json#L3130) | `inspect_pe_resources` | 失败 | 1 | 0 | 0 | 0/1 |
| [74](./results.json#L3166) | `inspect_pe_certificates` | 通过 | 1 | 1 | 0 | 1/1 |
| [75](./results.json#L3203) | `inspect_windows_shortcut` | 通过 | 1 | 1 | 0 | 1/1 |
| [76](./results.json#L3240) | `inspect_ntfs_journal` | 通过 | 1 | 1 | 0 | 1/1 |
| [77](./results.json#L3277) | `inspect_elf_notes` | 通过 | 1 | 1 | 0 | 1/1 |
| [78](./results.json#L3314) | `inspect_kernel_build_config` | 通过 | 1 | 1 | 0 | 1/1 |
| [79](./results.json#L3351) | `inspect_kernel_module` | 通过 | 1 | 1 | 0 | 1/1 |
| [80](./results.json#L3388) | `inspect_devicetree` | 通过 | 1 | 1 | 0 | 1/1 |
| [81](./results.json#L3425) | `inspect_go_binary` | 通过 | 1 | 1 | 0 | 1/1 |
| [82](./results.json#L3462) | `inspect_rust_binary` | 通过 | 1 | 1 | 0 | 1/1 |
| [83](./results.json#L3499) | `inspect_erlang_beam` | 通过 | 1 | 1 | 0 | 1/1 |
| [84](./results.json#L3536) | `inspect_python_pyc` | 通过 | 1 | 1 | 0 | 1/1 |
| [85](./results.json#L3573) | `inspect_v8_code_cache` | 通过 | 1 | 1 | 0 | 1/1 |
| [86](./results.json#L3610) | `inspect_managed_artifact` | 失败 | 1 | 1 | 0 | 0/1 |
| [87](./results.json#L3652) | `compare_managed_members` | 通过 | 1 | 2 | 0 | 1/1 |
| [88](./results.json#L3694) | `inspect_managed_native_boundaries` | 通过 | 1 | 1 | 0 | 1/1 |
| [89](./results.json#L3731) | `verify_managed_native_boundaries` | 通过 | 1 | 5 | 0 | 1/1 |
| [90](./results.json#L3788) | `project_managed_application_graph` | 通过 | 1 | 2 | 0 | 1/1 |
| [91](./results.json#L3830) | `inspect_il2cpp_metadata` | 通过 | 1 | 1 | 0 | 1/1 |
| [92](./results.json#L3867) | `inspect_wasm_artifact` | 通过 | 1 | 1 | 0 | 1/1 |
| [93](./results.json#L3904) | `compare_wasm_interfaces` | 通过 | 1 | 3 | 0 | 2/2 |
| [94](./results.json#L3959) | `inspect_gpu_code_objects` | 通过 | 1 | 1 | 0 | 1/1 |
| [95](./results.json#L3996) | `inspect_model_artifact` | 通过 | 1 | 1 | 0 | 2/2 |
| [96](./results.json#L4041) | `inspect_artifact` | 通过 | 1 | 2 | 0 | 1/1 |
| [97](./results.json#L4083) | `extract_artifact` | 通过 | 1 | 3 | 0 | 2/2 |
| [98](./results.json#L4138) | `inspect_desktop_application` | 失败 | 1 | 1 | 0 | 0/1 |
| [99](./results.json#L4180) | `audit_release_exposure` | 通过 | 1 | 1 | 0 | 1/1 |
| [100](./results.json#L4217) | `inspect_sqlite_database` | 通过 | 1 | 1 | 0 | 1/1 |
| [101](./results.json#L4254) | `get_evidence_bundle` | 通过 | 1 | 1 | 0 | 1/1 |
| [102](./results.json#L4291) | `export_evidence_bundle` | 通过 | 1 | 1 | 0 | 1/1 |
| [103](./results.json#L4328) | `import_evidence_bundle` | 通过 | 1 | 1 | 0 | 1/1 |
| [104](./results.json#L4365) | `compare_bundles` | 通过 | 1 | 1 | 0 | 1/1 |
| [105](./results.json#L4402) | `compare_artifacts` | 通过 | 1 | 2 | 0 | 1/1 |
| [106](./results.json#L4444) | `compare_process_captures` | 通过 | 1 | 2 | 0 | 1/1 |
| [107](./results.json#L4486) | `find_changed_behavior` | 通过 | 1 | 4 | 0 | 1/1 |
| [108](./results.json#L4538) | `correlate_static_and_runtime` | 通过 | 1 | 3 | 0 | 1/1 |
| [109](./results.json#L4585) | `build_reconstruction_obligation_ledger` | 通过 | 1 | 1 | 0 | 1/1 |
| [110](./results.json#L4622) | `evaluate_reconstruction_coverage` | 通过 | 1 | 1 | 0 | 1/1 |
| [111](./results.json#L4659) | `verify_reconstruction` | 通过 | 1 | 3 | 0 | 1/1 |
| [112](./results.json#L4706) | `record_unknown` | 通过 | 1 | 1 | 0 | 2/2 |
| [113](./results.json#L4751) | `list_unknowns` | 通过 | 1 | 1 | 0 | 1/1 |
| [114](./results.json#L4788) | `update_unknown` | 通过 | 1 | 2 | 0 | 2/2 |
| [115](./results.json#L4838) | `verify_unknown_resolution` | 通过 | 1 | 2 | 0 | 1/1 |
| [116](./results.json#L4880) | `export_environment_bundle` | 通过 | 1 | 2 | 0 | 1/1 |
| [117](./results.json#L4922) | `reset_investigation` | 通过 | 1 | 6 | 0 | 1/1 |
| [118](./results.json#L4984) | `guided_workflows` | 通过 | 1 | 1 | 0 | 1/1 |
| [119](./results.json#L5021) | `search_guidance` | 通过 | 1 | 1 | 0 | 1/1 |
| [120](./results.json#L5058) | `read_guidance_section` | 通过 | 1 | 2 | 0 | 1/1 |
| [121](./results.json#L5100) | `inspect_analysis_settings` | 通过 | 1 | 1 | 0 | 1/1 |
| [122](./results.json#L5137) | `update_analysis_settings` | 通过 | 1 | 1 | 0 | 1/1 |
| [123](./results.json#L5174) | `inspect_analysis_view` | 通过 | 1 | 4 | 0 | 1/1 |
