# 第 86、98 条断言修订后的全量回归

2026-11-20（上海时间）。每个编号在所属批次运行一次。先逐项核对四条原文的复测结果，全部通过后另开全新的对话执行全量批次。

| 批次 | 首轮通过 | 实际 MCP 调用 | MCP 报错 | 仅发一次原文的对话 |
|---|---:|---:|---:|---:|
| 第 66、73、86、98 条复测 | 4/4 | 8 | 0 | 4 |
| 完整回归 | 123/123 | 223 | 0 | 123 |

全量首轮命中 139/139 条返回值断言。两批共核对 127 个不同的对话 ID。以下统计以脚本退出时的判定为准。

## 四条复测

第 66 条在同一地址回读到 `demo_entry` 并用空参数关闭。第 73 条成功返回 PE 资源树。两条在本次复测中均通过。第 86 条核对程序集名称 `Fixture.Managed`，第 98 条核对运行时候选字段的列表类型。断言分别接受完整返回中的字段和摘要返回中 `summary` 下的同一字段。

[断言版本](https://github.com/5yy5kwtb9b-dotcom/s-angd/blob/8d8b24a4951fe7142604dc85284db24b5201681b/tools/rea/regression/checks.tsv) · [四条复测明细](./pilot.json) · [两批汇总](./summary.json) · [123 条逐条记录](./results.json)

## 逐条结果

编号链接定位到该轮的调用顺序、逐项断言和最终答复。第 1–3 条为 Mac 替代工具。

| 编号 | 工具 | 首轮 | 消息数 | MCP 调用 | MCP 报错 | 断言命中 |
|---:|---|---|---:|---:|---:|---:|
| [1](./results.json#L3) | `inspect_packet_fields` | 通过 | 1 | 1 | 0 | 1/1 |
| [2](./results.json#L40) | `inspect_packet_capture` | 通过 | 1 | 1 | 0 | 1/1 |
| [3](./results.json#L86) | `inspect_pcap_capture` | 通过 | 1 | 1 | 0 | 2/2 |
| [4](./results.json#L131) | `inspect_pcap_client` | 通过 | 1 | 1 | 0 | 2/2 |
| [5](./results.json#L176) | `inspect_web_network_capture` | 通过 | 1 | 1 | 0 | 3/3 |
| [6](./results.json#L229) | `inspect_web_page` | 通过 | 1 | 1 | 0 | 1/1 |
| [7](./results.json#L266) | `inspect_web_event_listeners` | 通过 | 1 | 1 | 0 | 1/1 |
| [8](./results.json#L303) | `capture_web_screenshot` | 通过 | 1 | 1 | 0 | 1/1 |
| [9](./results.json#L340) | `compare_web_screenshots` | 通过 | 1 | 1 | 0 | 1/1 |
| [10](./results.json#L377) | `observe_web_session` | 通过 | 1 | 1 | 0 | 1/1 |
| [11](./results.json#L414) | `compare_web_captures` | 通过 | 1 | 1 | 0 | 1/1 |
| [12](./results.json#L451) | `discover_webmcp_tools` | 通过 | 1 | 1 | 0 | 1/1 |
| [13](./results.json#L488) | `inspect_playwright_trace` | 通过 | 1 | 1 | 0 | 1/1 |
| [14](./results.json#L525) | `inspect_electron_page` | 通过 | 1 | 1 | 0 | 1/1 |
| [15](./results.json#L562) | `inspect_electron_fuses` | 通过 | 1 | 1 | 0 | 1/1 |
| [16](./results.json#L599) | `analyze_javascript_application` | 通过 | 1 | 1 | 0 | 1/1 |
| [17](./results.json#L636) | `trace_application_feature` | 通过 | 1 | 2 | 0 | 1/1 |
| [18](./results.json#L678) | `trace_javascript_semantics` | 通过 | 1 | 2 | 0 | 1/1 |
| [19](./results.json#L720) | `trace_web_module_imports` | 通过 | 1 | 1 | 0 | 1/1 |
| [20](./results.json#L757) | `trace_web_source_location` | 通过 | 1 | 1 | 0 | 1/1 |
| [21](./results.json#L794) | `export_web_scripts` | 通过 | 1 | 1 | 0 | 1/1 |
| [22](./results.json#L831) | `compare_source_to_bundle` | 通过 | 1 | 2 | 0 | 1/1 |
| [23](./results.json#L873) | `compare_application_versions` | 通过 | 1 | 4 | 0 | 2/2 |
| [24](./results.json#L933) | `compare_javascript_export_shapes` | 通过 | 1 | 3 | 0 | 1/1 |
| [25](./results.json#L980) | `observe_javascript_runtime` | 通过 | 1 | 1 | 0 | 1/1 |
| [26](./results.json#L1017) | `reconcile_javascript_runtime` | 通过 | 1 | 3 | 0 | 1/1 |
| [27](./results.json#L1064) | `compare_static_and_observed_endpoints` | 通过 | 1 | 3 | 0 | 1/1 |
| [28](./results.json#L1111) | `inspect_api_contract` | 通过 | 1 | 1 | 0 | 1/1 |
| [29](./results.json#L1148) | `inspect_android_package` | 通过 | 1 | 1 | 0 | 1/1 |
| [30](./results.json#L1185) | `inspect_apk_signature` | 通过 | 1 | 1 | 0 | 1/1 |
| [31](./results.json#L1222) | `search_android_classes` | 通过 | 1 | 1 | 0 | 1/1 |
| [32](./results.json#L1259) | `inspect_android_class` | 通过 | 1 | 1 | 0 | 1/1 |
| [33](./results.json#L1296) | `inspect_apktool_client` | 通过 | 1 | 1 | 0 | 1/1 |
| [34](./results.json#L1333) | `decode_android_resources` | 通过 | 1 | 2 | 0 | 2/2 |
| [35](./results.json#L1383) | `inspect_adb_client` | 通过 | 1 | 1 | 0 | 1/1 |
| [36](./results.json#L1420) | `list_adb_devices` | 通过 | 1 | 1 | 0 | 1/1 |
| [37](./results.json#L1457) | `project_android_application_graph` | 通过 | 1 | 4 | 0 | 1/1 |
| [38](./results.json#L1509) | `identify_flutter_build` | 通过 | 1 | 1 | 0 | 1/1 |
| [39](./results.json#L1546) | `inspect_dart_aot` | 通过 | 1 | 1 | 0 | 1/1 |
| [40](./results.json#L1583) | `project_harmony_application_graph` | 通过 | 1 | 4 | 0 | 1/1 |
| [41](./results.json#L1635) | `project_apple_application_graph` | 通过 | 1 | 4 | 0 | 1/1 |
| [42](./results.json#L1687) | `open_bundle_resources` | 通过 | 1 | 1 | 0 | 1/1 |
| [43](./results.json#L1724) | `decode_interface_builder` | 通过 | 1 | 2 | 0 | 1/1 |
| [44](./results.json#L1766) | `inspect_asset_catalog` | 通过 | 1 | 3 | 0 | 1/1 |
| [45](./results.json#L1813) | `inspect_keyed_archive` | 通过 | 1 | 2 | 0 | 1/1 |
| [46](./results.json#L1855) | `inspect_plist` | 通过 | 1 | 2 | 0 | 1/1 |
| [47](./results.json#L1897) | `inspect_macho` | 通过 | 1 | 3 | 0 | 2/2 |
| [48](./results.json#L1952) | `inspect_signature` | 通过 | 1 | 3 | 0 | 1/1 |
| [49](./results.json#L1999) | `inspect_apple_ips` | 通过 | 1 | 1 | 0 | 1/1 |
| [50](./results.json#L2036) | `demangle_swift` | 通过 | 1 | 2 | 0 | 1/1 |
| [51](./results.json#L2078) | `analyze_swift_types` | 通过 | 1 | 2 | 0 | 1/1 |
| [52](./results.json#L2120) | `get_objc_classes` | 通过 | 1 | 2 | 0 | 1/1 |
| [53](./results.json#L2162) | `get_objc_protocols` | 通过 | 1 | 2 | 0 | 1/1 |
| [54](./results.json#L2204) | `open_binary` | 通过 | 1 | 2 | 0 | 1/1 |
| [55](./results.json#L2246) | `binary_session` | 通过 | 1 | 1 | 0 | 1/1 |
| [56](./results.json#L2283) | `close_binary` | 通过 | 1 | 5 | 0 | 1/1 |
| [57](./results.json#L2340) | `binary_overview` | 通过 | 1 | 3 | 0 | 2/2 |
| [58](./results.json#L2395) | `list_architectures` | 通过 | 1 | 3 | 0 | 2/2 |
| [59](./results.json#L2450) | `list_documents` | 通过 | 1 | 2 | 0 | 1/1 |
| [60](./results.json#L2492) | `list_segments` | 通过 | 1 | 4 | 0 | 1/1 |
| [61](./results.json#L2544) | `list_procedures` | 通过 | 1 | 3 | 0 | 1/1 |
| [62](./results.json#L2591) | `search_procedures` | 通过 | 1 | 4 | 0 | 1/1 |
| [63](./results.json#L2643) | `list_names` | 通过 | 1 | 3 | 0 | 1/1 |
| [64](./results.json#L2690) | `address_name` | 通过 | 1 | 4 | 0 | 1/1 |
| [65](./results.json#L2742) | `inspect_address_context` | 通过 | 1 | 4 | 0 | 1/1 |
| [66](./results.json#L2794) | `set_address_name` | 通过 | 1 | 5 | 0 | 1/1 |
| [67](./results.json#L2856) | `set_addresses_names` | 通过 | 1 | 4 | 0 | 2/2 |
| [68](./results.json#L2916) | `list_cutter_sessions` | 通过 | 1 | 1 | 0 | 1/1 |
| [69](./results.json#L2953) | `inspect_native_exports` | 通过 | 1 | 1 | 0 | 1/1 |
| [70](./results.json#L2990) | `inspect_binary_hardening` | 通过 | 1 | 1 | 0 | 1/1 |
| [71](./results.json#L3027) | `inspect_byte_entropy` | 通过 | 1 | 1 | 0 | 1/1 |
| [72](./results.json#L3064) | `inspect_pe_imports` | 通过 | 1 | 1 | 0 | 2/2 |
| [73](./results.json#L3109) | `inspect_pe_resources` | 通过 | 1 | 1 | 0 | 1/1 |
| [74](./results.json#L3146) | `inspect_pe_certificates` | 通过 | 1 | 1 | 0 | 1/1 |
| [75](./results.json#L3183) | `inspect_windows_shortcut` | 通过 | 1 | 1 | 0 | 1/1 |
| [76](./results.json#L3220) | `inspect_ntfs_journal` | 通过 | 1 | 1 | 0 | 1/1 |
| [77](./results.json#L3257) | `inspect_elf_notes` | 通过 | 1 | 1 | 0 | 1/1 |
| [78](./results.json#L3294) | `inspect_kernel_build_config` | 通过 | 1 | 1 | 0 | 1/1 |
| [79](./results.json#L3331) | `inspect_kernel_module` | 通过 | 1 | 1 | 0 | 1/1 |
| [80](./results.json#L3368) | `inspect_devicetree` | 通过 | 1 | 1 | 0 | 1/1 |
| [81](./results.json#L3405) | `inspect_go_binary` | 通过 | 1 | 1 | 0 | 1/1 |
| [82](./results.json#L3442) | `inspect_rust_binary` | 通过 | 1 | 1 | 0 | 1/1 |
| [83](./results.json#L3479) | `inspect_erlang_beam` | 通过 | 1 | 1 | 0 | 1/1 |
| [84](./results.json#L3516) | `inspect_python_pyc` | 通过 | 1 | 1 | 0 | 1/1 |
| [85](./results.json#L3553) | `inspect_v8_code_cache` | 通过 | 1 | 1 | 0 | 1/1 |
| [86](./results.json#L3590) | `inspect_managed_artifact` | 通过 | 1 | 1 | 0 | 1/1 |
| [87](./results.json#L3627) | `compare_managed_members` | 通过 | 1 | 2 | 0 | 1/1 |
| [88](./results.json#L3669) | `inspect_managed_native_boundaries` | 通过 | 1 | 1 | 0 | 1/1 |
| [89](./results.json#L3706) | `verify_managed_native_boundaries` | 通过 | 1 | 5 | 0 | 1/1 |
| [90](./results.json#L3763) | `project_managed_application_graph` | 通过 | 1 | 2 | 0 | 1/1 |
| [91](./results.json#L3805) | `inspect_il2cpp_metadata` | 通过 | 1 | 1 | 0 | 1/1 |
| [92](./results.json#L3842) | `inspect_wasm_artifact` | 通过 | 1 | 1 | 0 | 1/1 |
| [93](./results.json#L3879) | `compare_wasm_interfaces` | 通过 | 1 | 3 | 0 | 2/2 |
| [94](./results.json#L3934) | `inspect_gpu_code_objects` | 通过 | 1 | 1 | 0 | 1/1 |
| [95](./results.json#L3971) | `inspect_model_artifact` | 通过 | 1 | 1 | 0 | 2/2 |
| [96](./results.json#L4016) | `inspect_artifact` | 通过 | 1 | 2 | 0 | 1/1 |
| [97](./results.json#L4058) | `extract_artifact` | 通过 | 1 | 3 | 0 | 2/2 |
| [98](./results.json#L4113) | `inspect_desktop_application` | 通过 | 1 | 1 | 0 | 1/1 |
| [99](./results.json#L4150) | `audit_release_exposure` | 通过 | 1 | 1 | 0 | 1/1 |
| [100](./results.json#L4187) | `inspect_sqlite_database` | 通过 | 1 | 1 | 0 | 1/1 |
| [101](./results.json#L4224) | `get_evidence_bundle` | 通过 | 1 | 1 | 0 | 1/1 |
| [102](./results.json#L4261) | `export_evidence_bundle` | 通过 | 1 | 1 | 0 | 1/1 |
| [103](./results.json#L4298) | `import_evidence_bundle` | 通过 | 1 | 1 | 0 | 1/1 |
| [104](./results.json#L4335) | `compare_bundles` | 通过 | 1 | 1 | 0 | 1/1 |
| [105](./results.json#L4372) | `compare_artifacts` | 通过 | 1 | 2 | 0 | 1/1 |
| [106](./results.json#L4414) | `compare_process_captures` | 通过 | 1 | 2 | 0 | 1/1 |
| [107](./results.json#L4456) | `find_changed_behavior` | 通过 | 1 | 4 | 0 | 1/1 |
| [108](./results.json#L4508) | `correlate_static_and_runtime` | 通过 | 1 | 3 | 0 | 1/1 |
| [109](./results.json#L4555) | `build_reconstruction_obligation_ledger` | 通过 | 1 | 1 | 0 | 1/1 |
| [110](./results.json#L4592) | `evaluate_reconstruction_coverage` | 通过 | 1 | 1 | 0 | 1/1 |
| [111](./results.json#L4629) | `verify_reconstruction` | 通过 | 1 | 3 | 0 | 1/1 |
| [112](./results.json#L4676) | `record_unknown` | 通过 | 1 | 1 | 0 | 2/2 |
| [113](./results.json#L4721) | `list_unknowns` | 通过 | 1 | 1 | 0 | 1/1 |
| [114](./results.json#L4758) | `update_unknown` | 通过 | 1 | 2 | 0 | 2/2 |
| [115](./results.json#L4808) | `verify_unknown_resolution` | 通过 | 1 | 2 | 0 | 1/1 |
| [116](./results.json#L4850) | `export_environment_bundle` | 通过 | 1 | 2 | 0 | 1/1 |
| [117](./results.json#L4892) | `reset_investigation` | 通过 | 1 | 6 | 0 | 1/1 |
| [118](./results.json#L4954) | `guided_workflows` | 通过 | 1 | 1 | 0 | 1/1 |
| [119](./results.json#L4991) | `search_guidance` | 通过 | 1 | 1 | 0 | 1/1 |
| [120](./results.json#L5028) | `read_guidance_section` | 通过 | 1 | 2 | 0 | 1/1 |
| [121](./results.json#L5070) | `inspect_analysis_settings` | 通过 | 1 | 1 | 0 | 1/1 |
| [122](./results.json#L5107) | `update_analysis_settings` | 通过 | 1 | 1 | 0 | 1/1 |
| [123](./results.json#L5144) | `inspect_analysis_view` | 通过 | 1 | 4 | 0 | 1/1 |
