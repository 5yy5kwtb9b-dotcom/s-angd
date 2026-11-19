# 11 条准备指令的 MCP 零报错复测

2026-11-20，macOS 上已配置 REA 的 Codex。本次使用 13 个全新 Codex 对话，每个对话只发送一次对应版本的指令。修订后首次复测有 9/11 条完成目标且全程 MCP 零报错，最终指令达到 11/11 条。

每个对话从仓库的 ZIP 和说明文件开始，自行解压并准备前序结果。逐项核对模型答复和实际工具返回。错误次数覆盖准备、目标及收尾的所有 MCP 调用；另一次成功调用不会抵消同一轮先前的错误。

| 原编号 | 最终指令 | 上轮实际报错原因与修订 | MCP 报错次数（上轮 → 本次各轮） |
|---:|---|---|---|
| 17 | [`trace_application_feature`](./Codex样例与会话准备.md#item-17) | application 只传 ID 时缺少证据字段，改传整图又超出输入上限。改用带 kind 的应用图引用。 | 2 → 0 |
| 18 | [`trace_javascript_semantics`](./Codex样例与会话准备.md#item-18) | 语义查询也先传了不完整的证据，再传整图时超限。把应用图引用和 return 节点 ID 分别写在对应位置。 | 2 → 0 |
| 22 | [`compare_source_to_bundle`](./Codex样例与会话准备.md#item-22) | application.kind 写成 retained。改用 retained-evidence，并给历史源码图单独传文件路径。 | 1 → 0 |
| 23 | [`compare_application_versions`](./Codex样例与会话准备.md#item-23) | 左右两侧只传了 evidence_id 或 parent_evidence_id。分别取两版摘要的父 ID，用带 kind 的 left、right 引用提交。首次复测中我给比较调用多写了 detail，最终版已删去该字段。 | 2 → 1 → 0 |
| 24 | [`compare_javascript_export_shapes`](./Codex样例与会话准备.md#item-24) | 两版证据引用缺少 kind。为每侧写明引用、模块路径和导出名。 | 2 → 0 |
| 26 | [`reconcile_javascript_runtime`](./Codex样例与会话准备.md#item-26) | 静态层缺少 analysis 层级，后续用了无效的引用、证据查询 detail 值和超限的整图。直接引用本轮应用图和 V8 观测。 | 6 → 0 |
| 27 | [`compare_static_and_observed_endpoints`](./Codex样例与会话准备.md#item-27) | 应用图和 HAR 均只传 ID，证据校验失败。分别用 application、capture 引用两项摘要的父记录。首次复测时 HAR 路径被填入 input_path，最终版明确使用 capture_path。 | 1 → 1 → 0 |
| 67 | [`set_addresses_names`](./Codex样例与会话准备.md#item-67) | 改名已成功，关闭时额外传入 snapshot_path，后端拒绝保存已改动元数据的快照。回读改名结果后以空参数关闭临时目标。 | 1 → 0 |
| 89 | [`verify_managed_native_boundaries`](./Codex样例与会话准备.md#item-89) | P/Invoke 与 Mach-O 证据只传 ID，补查时 get_evidence_bundle 使用了无效的 complete 选项。直接引用同一会话的两项证据。 | 3 → 0 |
| 93 | [`compare_wasm_interfaces`](./Codex样例与会话准备.md#item-93) | 左右证据先缺少 kind，后又填为 evidence_ref。两侧使用 retained-evidence 并固定旧左新右。 | 2 → 0 |
| 116 | [`export_environment_bundle`](./Codex样例与会话准备.md#item-116) | 导出时 source 只传了 evidence_id。写明来源引用的 kind，以及尚不存在的输出目录。 | 1 → 0 |

[逐次调用记录](./11条指令MCP零报错复测.json) · [上一轮 58 条的结果](./58条准备指令全新对话实测.md)
