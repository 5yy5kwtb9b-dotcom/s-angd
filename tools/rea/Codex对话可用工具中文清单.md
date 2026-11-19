# Codex 对话可用工具中文清单

本机累计实测 **123 项**，其中 **120 项来自 REA 6.9.0**，**3 项由 Mac 的本地 Wireshark 服务替代**。仅列入已通过 Codex 对话的工具连接得到有效返回的项目。不同工具使用各自支持的样例、后端或会话；部分验证使用空证据包、空设备列表或合成记录。

在对话中说出服务名、工具名和要处理的对象即可。例如：“用 mac_pcap 的 inspect_packet_capture 读取这个抓包里前 10 帧的帧号和长度。”表中的 **Mac 替代** 均调用 `mac_pcap`；其余各项调用 `rea`。

## 分类索引

| 功能分类 | REA | Mac 替代 | 合计 |
|---|---:|---:|---:|
| [抓包与网络记录](#group-1) | 2 | 3 | 5 |
| [网页、浏览器与 Electron](#group-2) | 10 | 0 | 10 |
| [JavaScript、源码映射与 API](#group-3) | 13 | 0 | 13 |
| [Android、ADB、Flutter 与鸿蒙](#group-4) | 12 | 0 | 12 |
| [Apple 应用、Swift 与 Objective-C](#group-5) | 13 | 0 | 13 |
| [原生二进制、符号与分析会话](#group-6) | 18 | 0 | 18 |
| [Windows、Linux 与设备文件](#group-7) | 9 | 0 | 9 |
| [编程语言、托管代码与计算模型](#group-8) | 15 | 0 | 15 |
| [文件、应用包与数据库](#group-9) | 5 | 0 | 5 |
| [证据、版本差异与重建验证](#group-10) | 17 | 0 | 17 |
| [工作指南、设置与结果浏览](#group-11) | 6 | 0 | 6 |
| **合计** | **120** | **3** | **123** |

<a name="group-1"></a>

## 抓包与网络记录（5 项）

3 项 Mac 替代工具复用 Wireshark 4.6.10。文件分析支持本地未压缩的 pcap 和 pcapng，单文件上限 32 MiB，逐包读取每次最多 500 帧。实测样例共 2 帧，长度分别为 60 和 74 字节。[工具实现与样例](./mac-pcap/) · [三次对话调用记录](./mac-pcap/Codex对话实测.json)

| 序号 | 工具名 | 中文用途 | 来源 |
|---:|---|---|---|
| 1 | `inspect_packet_fields` | 按字段名前缀查 Wireshark 字段及英文名称，例如查询 frame.len。 | **Mac 替代** |
| 2 | `inspect_packet_capture` | 从离线抓包逐帧读取指定字段，可按 Wireshark 显示过滤器筛选。 | **Mac 替代** |
| 3 | `inspect_pcap_capture` | 汇总离线抓包的格式、链路类型、包数、文件大小、线上字节数和时长。 | **Mac 替代** |
| 4 | `inspect_pcap_client` | 检查本机 TShark 和 capinfos 的路径及版本。 | REA |
| 5 | `inspect_web_network_capture` | 读取已保存的 HAR 等网络记录，查看其中的请求和事件。 | REA |

<a name="group-2"></a>

## 网页、浏览器与 Electron（10 项）

| 序号 | 工具名 | 中文用途 | 来源 |
|---:|---|---|---|
| 6 | `inspect_web_page` | 查看已连接浏览器页面的结构与资源。 | REA |
| 7 | `inspect_web_event_listeners` | 查看指定页面元素直接注册的事件监听器及回调来源。 | REA |
| 8 | `capture_web_screenshot` | 截取当前网页可见区域，返回 PNG 图像。 | REA |
| 9 | `compare_web_screenshots` | 逐像素比较两张网页截图，统计变化比例和通道差异。 | REA |
| 10 | `observe_web_session` | 在指定时段记录用户操作网页时发生的浏览器事件。 | REA |
| 11 | `compare_web_captures` | 比较两次页面检查或两段已录制的浏览器场景。 | REA |
| 12 | `discover_webmcp_tools` | 列出网页声明的 WebMCP 工具及输入参数结构。 | REA |
| 13 | `inspect_playwright_trace` | 检查已保存的 Playwright 跟踪记录。 | REA |
| 14 | `inspect_electron_page` | 查看已连接的 Electron 本地文件页面及其框架信息。 | REA |
| 15 | `inspect_electron_fuses` | 读取 Electron 安装包中编译固化的功能开关。 | REA |

<a name="group-3"></a>

## JavaScript、源码映射与 API（13 项）

| 序号 | 工具名 | 中文用途 | 来源 |
|---:|---|---|---|
| 16 | `analyze_javascript_application` | 静态分析 JavaScript 应用，生成模块、依赖等关系图。 | REA |
| 17 | `trace_application_feature` | 从指定起点沿 JavaScript 应用关系图追踪一项功能。 | REA |
| 18 | `trace_javascript_semantics` | 追踪静态数据流、直接调用、返回值和闭包关系。 | REA |
| 19 | `trace_web_module_imports` | 从已导出脚本追踪 ES 模块导入和再导出的来源。 | REA |
| 20 | `trace_web_source_location` | 利用本地 source map 将生成脚本的行列位置映射回源码。 | REA |
| 21 | `export_web_scripts` | 将网页记录中已保存的 JavaScript 导出为脚本文件和校验清单。 | REA |
| 22 | `compare_source_to_bundle` | 对照历史源码和打包产物，识别保留、变更及无法匹配的部分。 | REA |
| 23 | `compare_application_versions` | 对比两个版本的 JavaScript 应用关系图，列出新增、删除和变化。 | REA |
| 24 | `compare_javascript_export_shapes` | 比较两个 JavaScript 模块指定导出项的静态返回属性结构。 | REA |
| 25 | `observe_javascript_runtime` | 查看本机 Node 或 Electron 运行时已载入的脚本与执行上下文。 | REA |
| 26 | `reconcile_javascript_runtime` | 对照 JavaScript 静态关系图与已有运行时观测记录。 | REA |
| 27 | `compare_static_and_observed_endpoints` | 将代码中声明的接口与 HAR 实际记录的请求配对。 | REA |
| 28 | `inspect_api_contract` | 从本地 OpenAPI JSON 或 GraphQL SDL 读取接口声明。 | REA |

<a name="group-4"></a>

## Android、ADB、Flutter 与鸿蒙（12 项）

| 序号 | 工具名 | 中文用途 | 来源 |
|---:|---|---|---|
| 29 | `inspect_android_package` | 读取 APK 的包名、SDK、权限、组件以及类和资源数量。 | REA |
| 30 | `inspect_apk_signature` | 查看 APK 声明的签名方案、签名者和证书指纹。 | REA |
| 31 | `search_android_classes` | 在 APK 的顶层类名中按子串搜索。 | REA |
| 32 | `inspect_android_class` | 查看指定 Android 类的方法、字段、内部类和 DEX 类型信息。 | REA |
| 33 | `inspect_apktool_client` | 检查本机 Apktool 的启动命令和版本。 | REA |
| 34 | `decode_android_resources` | 解码 APK 的清单、字符串和多语言资源。 | REA |
| 35 | `inspect_adb_client` | 查看本机 ADB 客户端的位置及版本。 | REA |
| 36 | `list_adb_devices` | 列出 ADB 报告的设备及连接状态，空列表也是有效结果。 | REA |
| 37 | `project_android_application_graph` | 从 APK 的文件清单整理组件、文件摘要和运行时线索。 | REA |
| 38 | `identify_flutter_build` | 识别 Flutter 构建的架构、Dart 快照和引擎标识。 | REA |
| 39 | `inspect_dart_aot` | 检查受支持的旧版 Android Dart AOT 快照结构。 | REA |
| 40 | `project_harmony_application_graph` | 从 HAP、HSP 或 App Pack 清单整理鸿蒙组件与子包关系。 | REA |

<a name="group-5"></a>

## Apple 应用、Swift 与 Objective-C（13 项）

| 序号 | 工具名 | 中文用途 | 来源 |
|---:|---|---|---|
| 41 | `project_apple_application_graph` | 从 IPA、应用包或磁盘映像的清单整理 Apple 应用及嵌套包关系。 | REA |
| 42 | `open_bundle_resources` | 在会话中以只读方式打开 Apple 应用包资源。 | REA |
| 43 | `decode_interface_builder` | 解码已编译的 storyboard 和 nib，列出界面对象、层级与连接。 | REA |
| 44 | `inspect_asset_catalog` | 检查 Apple 应用的资源目录及其中的资源条目。 | REA |
| 45 | `inspect_keyed_archive` | 读取 Apple 键值归档中的对象和引用关系。 | REA |
| 46 | `inspect_plist` | 读取 Apple 属性列表中的键、值与结构。 | REA |
| 47 | `inspect_macho` | 查看 Mach-O 可执行文件或架构切片的结构信息。 | REA |
| 48 | `inspect_signature` | 查看 Mach-O 切片的签名身份、授权项和强化运行时状态。 | REA |
| 49 | `inspect_apple_ips` | 从 Apple IPS 崩溃报告中读取异常、线程和加载映像。 | REA |
| 50 | `demangle_swift` | 将 Swift 编译符号还原为可读名称。 | REA |
| 51 | `analyze_swift_types` | 整理二进制中的 Swift 类型信息。 | REA |
| 52 | `get_objc_classes` | 列出二进制中的 Objective-C 类信息。 | REA |
| 53 | `get_objc_protocols` | 列出二进制中的 Objective-C 协议信息。 | REA |

<a name="group-6"></a>

## 原生二进制、符号与分析会话（18 项）

| 序号 | 工具名 | 中文用途 | 来源 |
|---:|---|---|---|
| 54 | `open_binary` | 打开本地二进制或分析数据库，选定分析后端。 | REA |
| 55 | `binary_session` | 查看当前分析目标、后端及其可用能力。 | REA |
| 56 | `close_binary` | 关闭当前二进制分析目标并释放引擎资源。 | REA |
| 57 | `binary_overview` | 获取当前二进制的结构概览。 | REA |
| 58 | `list_architectures` | 列出目标文件包含的处理器架构。 | REA |
| 59 | `list_documents` | 列出分析后端可见的文档。 | REA |
| 60 | `list_segments` | 列出当前二进制的内存段。 | REA |
| 61 | `list_procedures` | 列出后端已识别的函数。 | REA |
| 62 | `search_procedures` | 按条件搜索已识别的函数。 | REA |
| 63 | `list_names` | 列出已命名的地址和符号。 | REA |
| 64 | `address_name` | 查询一个地址对应的符号名。 | REA |
| 65 | `inspect_address_context` | 查看指定地址的名称、所属函数及后端可提供的上下文。 | REA |
| 66 | `set_address_name` | 在分析会话中修改一个地址的符号名。 | REA |
| 67 | `set_addresses_names` | 在分析会话中批量修改地址的符号名。 | REA |
| 68 | `list_cutter_sessions` | 列出本机可发现的 Cutter 桥接会话。 | REA |
| 69 | `inspect_native_exports` | 读取 PE 导出项或 ELF 动态导出符号。 | REA |
| 70 | `inspect_binary_hardening` | 查看 ELF、PE 或 Mach-O 声明的二进制安全加固特性。 | REA |
| 71 | `inspect_byte_entropy` | 计算文件整体或指定区域的字节熵，观察字节分布。 | REA |

<a name="group-7"></a>

## Windows、Linux 与设备文件（9 项）

| 序号 | 工具名 | 中文用途 | 来源 |
|---:|---|---|---|
| 72 | `inspect_pe_imports` | 列出 Windows PE 导入的 DLL 及其函数。 | REA |
| 73 | `inspect_pe_resources` | 查看 PE 资源树中的类型、名称、语言和数据范围。 | REA |
| 74 | `inspect_pe_certificates` | 查看 PE 证书表及其中记录的签名者和算法。 | REA |
| 75 | `inspect_windows_shortcut` | 读取 Windows 快捷方式记录的路径、参数和工作目录。 | REA |
| 76 | `inspect_ntfs_journal` | 检查 NTFS 变更日志记录。 | REA |
| 77 | `inspect_elf_notes` | 读取 ELF 注记的类型、所有者及数据范围。 | REA |
| 78 | `inspect_kernel_build_config` | 从 Linux 内核映像读取构建标识及嵌入的内核配置。 | REA |
| 79 | `inspect_kernel_module` | 查看 Linux 内核模块的元数据、符号和签名区信息。 | REA |
| 80 | `inspect_devicetree` | 解析扁平设备树，查看硬件节点、属性和内存保留区。 | REA |

<a name="group-8"></a>

## 编程语言、托管代码与计算模型（15 项）

| 序号 | 工具名 | 中文用途 | 来源 |
|---:|---|---|---|
| 81 | `inspect_go_binary` | 从 Go 二进制读取编译器、模块、依赖及构建参数。 | REA |
| 82 | `inspect_rust_binary` | 从含 cargo-auditable 元数据的 Rust 二进制读取依赖。 | REA |
| 83 | `inspect_erlang_beam` | 解析 Erlang BEAM 文件中的数据块、原子和导入导出项。 | REA |
| 84 | `inspect_python_pyc` | 静态读取 CPython 字节码文件头、代码对象及常量摘要。 | REA |
| 85 | `inspect_v8_code_cache` | 查看 V8 或 bytenode 代码缓存的文件头和结构。 | REA |
| 86 | `inspect_managed_artifact` | 查看 .NET 托管程序集的标识与 PE/CLI 元数据。 | REA |
| 87 | `compare_managed_members` | 对比两组已有的托管成员记录，识别对应成员及差异。 | REA |
| 88 | `inspect_managed_native_boundaries` | 查看 .NET 程序集中的 P/Invoke 等原生调用声明。 | REA |
| 89 | `verify_managed_native_boundaries` | 将托管调用声明与已有的原生导出或函数记录核对。 | REA |
| 90 | `project_managed_application_graph` | 将托管程序集、成员及原生调用关系整理为应用关系图。 | REA |
| 91 | `inspect_il2cpp_metadata` | 查看 Unity IL2CPP 元数据表及可关联的原生方法。 | REA |
| 92 | `inspect_wasm_artifact` | 使用 WABT 验证 WebAssembly 模块并查看段、导入导出和 WAT 表示。 | REA |
| 93 | `compare_wasm_interfaces` | 对比两个 WebAssembly 模块导入导出项的名称、种类和签名。 | REA |
| 94 | `inspect_gpu_code_objects` | 查看 CUDA 或 HIP 代码对象及内核条目。 | REA |
| 95 | `inspect_model_artifact` | 读取 GGUF 或 safetensors 模型的元数据和张量声明。 | REA |

<a name="group-9"></a>

## 文件、应用包与数据库（5 项）

| 序号 | 工具名 | 中文用途 | 来源 |
|---:|---|---|---|
| 96 | `inspect_artifact` | 识别本地文件或应用包，查看支持格式的内容清单。 | REA |
| 97 | `extract_artifact` | 从已打开的归档中将全部或选定文件解包到本地目录。 | REA |
| 98 | `inspect_desktop_application` | 从桌面应用目录识别可能使用的框架和运行时。 | REA |
| 99 | `audit_release_exposure` | 检查已发布应用包中仍可被静态读取的信息。 | REA |
| 100 | `inspect_sqlite_database` | 读取 SQLite 快照的表结构，可查看指定列和记录。 | REA |

<a name="group-10"></a>

## 证据、版本差异与重建验证（17 项）

本机实测中，证据包的导入、导出和对比使用临时会话的空包；进程对比和静态与运行时关联使用离线合成记录；环境包导出使用手写 HAR。

| 序号 | 工具名 | 中文用途 | 来源 |
|---:|---|---|---|
| 101 | `get_evidence_bundle` | 读取当前会话保留的分析证据及待解问题。 | REA |
| 102 | `export_evidence_bundle` | 把当前会话的证据包写入本地文件。 | REA |
| 103 | `import_evidence_bundle` | 校验证据包后，将其中的记录合并到当前会话。 | REA |
| 104 | `compare_bundles` | 比较两份分析证据包。 | REA |
| 105 | `compare_artifacts` | 比较两份分析产物记录中的差异。 | REA |
| 106 | `compare_process_captures` | 对比两份已有的进程观测记录。 | REA |
| 107 | `find_changed_behavior` | 汇总已有的进程、产物和函数比较结果，定位行为变化。 | REA |
| 108 | `correlate_static_and_runtime` | 用已有的静态和运行时比较结果核对指定的关联假设。 | REA |
| 109 | `build_reconstruction_obligation_ledger` | 整理重建工作需要验证的事项及相应证据。 | REA |
| 110 | `evaluate_reconstruction_coverage` | 检查指定范围的重建验证覆盖了哪些要求、还缺哪些证据。 | REA |
| 111 | `verify_reconstruction` | 按明确列出的行为和结构要求核验重建结果。 | REA |
| 112 | `record_unknown` | 将尚未解决的问题记入调查记录。 | REA |
| 113 | `list_unknowns` | 按状态、严重程度或领域列出待解问题。 | REA |
| 114 | `update_unknown` | 更新已记录问题的内容或处理状态。 | REA |
| 115 | `verify_unknown_resolution` | 对照证据核验某个问题是否满足结案条件。 | REA |
| 116 | `export_environment_bundle` | 将已保存的浏览器场景或 HAR 证据导出为本地环境包。 | REA |
| 117 | `reset_investigation` | 清空当前调查保留的证据和问题历史。 | REA |

<a name="group-11"></a>

## 工作指南、设置与结果浏览（6 项）

| 序号 | 工具名 | 中文用途 | 来源 |
|---:|---|---|---|
| 118 | `guided_workflows` | 浏览 REA 自带的工作流程及操作指南。 | REA |
| 119 | `search_guidance` | 按关键词查找已安装的 REA 指南章节。 | REA |
| 120 | `read_guidance_section` | 读取选定的指南章节。 | REA |
| 121 | `inspect_analysis_settings` | 查看分析的大小限制、超时和工作进程内存设置。 | REA |
| 122 | `update_analysis_settings` | 调整或重置后续分析任务使用的运行时设置。 | REA |
| 123 | `inspect_analysis_view` | 按视图读取已保留的分析结果，支持分段浏览。 | REA |
