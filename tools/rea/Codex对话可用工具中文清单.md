# Codex 对话可用工具中文清单

本机累计实测 **123 项**，其中 **120 项来自 REA 6.9.0**，**3 项由 Mac 的本地 Wireshark 服务替代**。仅列入已通过 Codex 对话的工具连接得到有效返回的项目。不同工具使用各自支持的样例、后端或会话；部分验证使用空证据包、空设备列表或合成记录。

在对话中说出服务名、工具名和要处理的对象即可。例如：“用 mac_pcap 的 inspect_packet_capture 读取这个抓包里前 10 帧的帧号和长度。”表中的 **Mac 替代** 均调用 `mac_pcap`；其余各项调用 `rea`。

每行最后一列都可以复制到 Codex。示例文件名可替换为自己的本地文件路径；抓包示例可使用[随附的两帧样例](./mac-pcap/两帧样例.pcap)。提到“当前”“上一条”或“本对话”的示例，请在相应的目标已打开或前一步结果就绪时使用。

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

| 序号 | 工具名 | 中文用途 | 来源 | 中文调用示例 |
|---:|---|---|---|---|
| 1 | `inspect_packet_fields` | 按字段名前缀查 Wireshark 字段及英文名称，例如查询 frame.len。 | **Mac 替代** | 请用 `mac_pcap` 的 `inspect_packet_fields` 查找以 frame.len 开头的 Wireshark 字段，告诉我哪个字段表示帧长。 |
| 2 | `inspect_packet_capture` | 从离线抓包逐帧读取指定字段，可按 Wireshark 显示过滤器筛选。 | **Mac 替代** | 请用 `mac_pcap` 的 `inspect_packet_capture` 读取我提供的《两帧样例.pcap》，按帧号列出 frame.number 和 frame.len。 |
| 3 | `inspect_pcap_capture` | 汇总离线抓包的格式、链路类型、包数、文件大小、线上字节数和时长。 | **Mac 替代** | 请用 `mac_pcap` 的 `inspect_pcap_capture` 汇总我提供的《两帧样例.pcap》，告诉我包数、线上字节总数和持续时间。 |
| 4 | `inspect_pcap_client` | 检查本机 TShark 和 capinfos 的路径及版本。 | REA | 请用 `rea` 的 `inspect_pcap_client` 检查这台 Mac 上 TShark 和 capinfos 的实际路径和版本。 |
| 5 | `inspect_web_network_capture` | 读取已保存的 HAR 等网络记录，查看其中的请求和事件。 | REA | 请用 `rea` 的 `inspect_web_network_capture` 读取我提供的 demo.har，按记录顺序列出前五个请求的方法、路径和响应状态码。 |

<a name="group-2"></a>

## 网页、浏览器与 Electron（10 项）

| 序号 | 工具名 | 中文用途 | 来源 | 中文调用示例 |
|---:|---|---|---|---|
| 6 | `inspect_web_page` | 查看已连接浏览器页面的结构与资源。 | REA | 请用 `rea` 的 `inspect_web_page` 检查我通过本机 CDP 连接并指定的测试页，告诉我页面标题和加载了哪些脚本。 |
| 7 | `inspect_web_event_listeners` | 查看指定页面元素直接注册的事件监听器及回调来源。 | REA | 请用 `rea` 的 `inspect_web_event_listeners` 查看指定 CDP 测试页上 #submit 按钮直接注册的监听器，列出事件类型及可定位的回调脚本。 |
| 8 | `capture_web_screenshot` | 截取当前网页可见区域，返回 PNG 图像。 | REA | 请用 `rea` 的 `capture_web_screenshot` 为我指定的本机 CDP 测试页截一张当前可见区域的 PNG。 |
| 9 | `compare_web_screenshots` | 逐像素比较两张网页截图，统计变化比例和通道差异。 | REA | 请用 `rea` 的 `compare_web_screenshots` 比较本对话中先后取得的两份 REA 网页截图，给出发生变化的像素占比。 |
| 10 | `observe_web_session` | 在指定时段记录用户操作网页时发生的浏览器事件。 | REA | 请用 `rea` 的 `observe_web_session` 在我操作指定的本机 CDP 测试页时观察 10 秒，按顺序概括记录到的页面事件。 |
| 11 | `compare_web_captures` | 比较两次页面检查或两段已录制的浏览器场景。 | REA | 请用 `rea` 的 `compare_web_captures` 对比本对话中改版前、改版后的两份页面检查结果，列出发生变化的页面资源。 |
| 12 | `discover_webmcp_tools` | 列出网页声明的 WebMCP 工具及输入参数结构。 | REA | 请用 `rea` 的 `discover_webmcp_tools` 查看我指定的本机 CDP 测试页声明了哪些 WebMCP 工具，给出名称和参数。 |
| 13 | `inspect_playwright_trace` | 检查已保存的 Playwright 跟踪记录。 | REA | 请用 `rea` 的 `inspect_playwright_trace` 读取我提供的 trace.zip，按记录顺序列出前十条网络事件。 |
| 14 | `inspect_electron_page` | 查看已连接的 Electron 本地文件页面及其框架信息。 | REA | 请用 `rea` 的 `inspect_electron_page` 使用我提供的本机 CDP 端点和目标 ID，查看 Electron 测试应用中本地文件页的主框架 URL。 |
| 15 | `inspect_electron_fuses` | 读取 Electron 安装包中编译固化的功能开关。 | REA | 请用 `rea` 的 `inspect_electron_fuses` 检查我提供的 Demo.app，列出其中 Electron 功能开关的名称和当前值。 |

<a name="group-3"></a>

## JavaScript、源码映射与 API（13 项）

| 序号 | 工具名 | 中文用途 | 来源 | 中文调用示例 |
|---:|---|---|---|---|
| 16 | `analyze_javascript_application` | 静态分析 JavaScript 应用，生成模块、依赖等关系图。 | REA | 请用 `rea` 的 `analyze_javascript_application` 分析我提供的 app.asar，列出入口模块及其直接导入的模块。 |
| 17 | `trace_application_feature` | 从指定起点沿 JavaScript 应用关系图追踪一项功能。 | REA | 请用 `rea` 的 `trace_application_feature` 在刚生成的 JavaScript 应用图中，以 renderer.js 模块为起点追踪它关联的功能。 |
| 18 | `trace_javascript_semantics` | 追踪静态数据流、直接调用、返回值和闭包关系。 | REA | 请用 `rea` 的 `trace_javascript_semantics` 使用我选中的语义节点 ID，在本对话的 JavaScript 应用图中向后追溯它的值来自哪里。 |
| 19 | `trace_web_module_imports` | 从已导出脚本追踪 ES 模块导入和再导出的来源。 | REA | 请用 `rea` 的 `trace_web_module_imports` 读取我提供的脚本导出清单 manifest.json，列出编号 0 的脚本导入了哪些模块。 |
| 20 | `trace_web_source_location` | 利用本地 source map 将生成脚本的行列位置映射回源码。 | REA | 请用 `rea` 的 `trace_web_source_location` 使用我提供的导出清单和配套 app.js.map，把编号 0 的脚本第 1 行、第 0 列映射回源码位置。 |
| 21 | `export_web_scripts` | 将网页记录中已保存的 JavaScript 导出为脚本文件和校验清单。 | REA | 请用 `rea` 的 `export_web_scripts` 从我提供的页面检查记录 capture.json 导出已保存的脚本，将脚本和清单写入工作区新目录 scripts-export。 |
| 22 | `compare_source_to_bundle` | 对照历史源码和打包产物，识别保留、变更及无法匹配的部分。 | REA | 请用 `rea` 的 `compare_source_to_bundle` 将我提供的历史源码图 HistoricalSourceGraph 与本对话的打包应用图比对，列出修改过的模块。 |
| 23 | `compare_application_versions` | 对比两个版本的 JavaScript 应用关系图，列出新增、删除和变化。 | REA | 请用 `rea` 的 `compare_application_versions` 比较本对话中旧版和新版的两份 JavaScript 应用图，分别列出新增和删除的模块。 |
| 24 | `compare_javascript_export_shapes` | 比较两个 JavaScript 模块指定导出项的静态返回属性结构。 | REA | 请用 `rea` 的 `compare_javascript_export_shapes` 对照本对话中新旧两份应用图，比较两版 profile.js 导出的 getProfile 返回哪些属性。 |
| 25 | `observe_javascript_runtime` | 查看本机 Node 或 Electron 运行时已载入的脚本与执行上下文。 | REA | 请用 `rea` 的 `observe_javascript_runtime` 使用我提供的本机 V8 Inspector 端点和目标 ID，列出 Node 测试进程已载入的脚本。 |
| 26 | `reconcile_javascript_runtime` | 对照 JavaScript 静态关系图与已有运行时观测记录。 | REA | 请用 `rea` 的 `reconcile_javascript_runtime` 对齐本对话的 JavaScript 静态应用图和已有的 V8 观测记录，列出两边都能确认的脚本。 |
| 27 | `compare_static_and_observed_endpoints` | 将代码中声明的接口与 HAR 实际记录的请求配对。 | REA | 请用 `rea` 的 `compare_static_and_observed_endpoints` 核对本对话的应用图与同一测试应用的 HAR 分析结果，列出代码声明且抓包中出现过的接口。 |
| 28 | `inspect_api_contract` | 从本地 OpenAPI JSON 或 GraphQL SDL 读取接口声明。 | REA | 请用 `rea` 的 `inspect_api_contract` 读取我提供的 openapi.json，按路径列出声明的 HTTP 方法。 |

<a name="group-4"></a>

## Android、ADB、Flutter 与鸿蒙（12 项）

| 序号 | 工具名 | 中文用途 | 来源 | 中文调用示例 |
|---:|---|---|---|---|
| 29 | `inspect_android_package` | 读取 APK 的包名、SDK、权限、组件以及类和资源数量。 | REA | 请用 `rea` 的 `inspect_android_package` 查看我提供的 demo.apk，列出包名、目标 SDK 和声明的权限。 |
| 30 | `inspect_apk_signature` | 查看 APK 声明的签名方案、签名者和证书指纹。 | REA | 请用 `rea` 的 `inspect_apk_signature` 读取我提供的 demo.apk，列出检测到的签名方案和签名证书指纹。 |
| 31 | `search_android_classes` | 在 APK 的顶层类名中按子串搜索。 | REA | 请用 `rea` 的 `search_android_classes` 在我提供的 demo.apk 中搜索名称含 Activity 的类，列出完整类名。 |
| 32 | `inspect_android_class` | 查看指定 Android 类的方法、字段、内部类和 DEX 类型信息。 | REA | 请用 `rea` 的 `inspect_android_class` 打开我提供的 demo.apk 中的 example.MainActivity，列出它声明的字段与方法。 |
| 33 | `inspect_apktool_client` | 检查本机 Apktool 的启动命令和版本。 | REA | 请用 `rea` 的 `inspect_apktool_client` 检查这台 Mac 实际使用的 Apktool 启动命令和版本。 |
| 34 | `decode_android_resources` | 解码 APK 的清单、字符串和多语言资源。 | REA | 请用 `rea` 的 `decode_android_resources` 解码我提供的 demo.apk，列出实际包含的语言资源，并从每种语言中举一个字符串示例。 |
| 35 | `inspect_adb_client` | 查看本机 ADB 客户端的位置及版本。 | REA | 请用 `rea` 的 `inspect_adb_client` 告诉我本机 ADB 客户端的安装位置和版本。 |
| 36 | `list_adb_devices` | 列出 ADB 报告的设备及连接状态，空列表也是有效结果。 | REA | 请用 `rea` 的 `list_adb_devices` 只列出 ADB 当前可见的设备和连接状态，若列表为空就告诉我。 |
| 37 | `project_android_application_graph` | 从 APK 的文件清单整理组件、文件摘要和运行时线索。 | REA | 请用 `rea` 的 `project_android_application_graph` 根据本对话里 demo.apk 的嵌套文件清单证据，列出组件路径及运行时线索。 |
| 38 | `identify_flutter_build` | 识别 Flutter 构建的架构、Dart 快照和引擎标识。 | REA | 请用 `rea` 的 `identify_flutter_build` 检查我提供的 Flutter 安装包 demo.apk，列出其中的 ABI 和可识别的 Dart 快照标识。 |
| 39 | `inspect_dart_aot` | 检查受支持的旧版 Android Dart AOT 快照结构。 | REA | 请用 `rea` 的 `inspect_dart_aot` 读取我提供的旧版 Flutter 测试 APK 中 arm64-v8a 的 Dart AOT 快照，概括可识别的结构。 |
| 40 | `project_harmony_application_graph` | 从 HAP、HSP 或 App Pack 清单整理鸿蒙组件与子包关系。 | REA | 请用 `rea` 的 `project_harmony_application_graph` 根据本对话里 demo.app 鸿蒙 App Pack 的嵌套清单证据，列出子包名称及路径。 |

<a name="group-5"></a>

## Apple 应用、Swift 与 Objective-C（13 项）

| 序号 | 工具名 | 中文用途 | 来源 | 中文调用示例 |
|---:|---|---|---|---|
| 41 | `project_apple_application_graph` | 从 IPA、应用包或磁盘映像的清单整理 Apple 应用及嵌套包关系。 | REA | 请用 `rea` 的 `project_apple_application_graph` 根据本对话里 Demo.ipa 的嵌套清单证据，列出主应用和内嵌扩展所在的目录。 |
| 42 | `open_bundle_resources` | 在会话中以只读方式打开 Apple 应用包资源。 | REA | 请用 `rea` 的 `open_bundle_resources` 以只读方式打开我提供的 Demo.app 资源目录，告诉我当前选中了哪个应用包。 |
| 43 | `decode_interface_builder` | 解码已编译的 storyboard 和 nib，列出界面对象、层级与连接。 | REA | 请用 `rea` 的 `decode_interface_builder` 查看当前已打开的 Demo.app 中编译后的 storyboard，列出可识别的界面层级和控件连接。 |
| 44 | `inspect_asset_catalog` | 检查 Apple 应用的资源目录及其中的资源条目。 | REA | 请用 `rea` 的 `inspect_asset_catalog` 查看当前已打开的 Demo.app 的资源目录，从第一项起列出最多十个资源条目。 |
| 45 | `inspect_keyed_archive` | 读取 Apple 键值归档中的对象和引用关系。 | REA | 请用 `rea` 的 `inspect_keyed_archive` 读取当前 Demo.app 中的 Contents/Resources/Model.plist 键值归档，列出根对象及其引用的类。 |
| 46 | `inspect_plist` | 读取 Apple 属性列表中的键、值与结构。 | REA | 请用 `rea` 的 `inspect_plist` 读取当前 Demo.app 的 Contents/Info.plist，告诉我 CFBundleIdentifier 和 CFBundleVersion。 |
| 47 | `inspect_macho` | 查看 Mach-O 可执行文件或架构切片的结构信息。 | REA | 请用 `rea` 的 `inspect_macho` 查看当前打开的 Mach-O 测试文件，列出所选切片的架构和加载命令。 |
| 48 | `inspect_signature` | 查看 Mach-O 切片的签名身份、授权项和强化运行时状态。 | REA | 请用 `rea` 的 `inspect_signature` 查看当前打开的 Mach-O 测试文件，告诉我签名身份和已声明的授权项。 |
| 49 | `inspect_apple_ips` | 从 Apple IPS 崩溃报告中读取异常、线程和加载映像。 | REA | 请用 `rea` 的 `inspect_apple_ips` 读取我提供的 Demo.ips 崩溃报告，找出异常类型和触发崩溃的线程。 |
| 50 | `demangle_swift` | 将 Swift 编译符号还原为可读名称。 | REA | 请用 `rea` 的 `demangle_swift` 把 Swift 符号 $s4Test3fooyyF 还原成可读名称。 |
| 51 | `analyze_swift_types` | 整理二进制中的 Swift 类型信息。 | REA | 请用 `rea` 的 `analyze_swift_types` 在当前打开的 Swift 测试程序里查找名称含 Account 的类。 |
| 52 | `get_objc_classes` | 列出二进制中的 Objective-C 类信息。 | REA | 请用 `rea` 的 `get_objc_classes` 在当前打开的测试程序中列出名称含 ViewController 的 Objective-C 类。 |
| 53 | `get_objc_protocols` | 列出二进制中的 Objective-C 协议信息。 | REA | 请用 `rea` 的 `get_objc_protocols` 列出当前打开的测试程序声明的 Objective-C 协议名称。 |

<a name="group-6"></a>

## 原生二进制、符号与分析会话（18 项）

| 序号 | 工具名 | 中文用途 | 来源 | 中文调用示例 |
|---:|---|---|---|---|
| 54 | `open_binary` | 打开本地二进制或分析数据库，选定分析后端。 | REA | 请用 `rea` 的 `open_binary` 用 Ghidra 打开我提供的 demo 原生测试程序，并报告识别到的文件格式。 |
| 55 | `binary_session` | 查看当前分析目标、后端及其可用能力。 | REA | 请用 `rea` 的 `binary_session` 告诉我当前 REA 会话选中哪个文件、使用哪个分析后端。 |
| 56 | `close_binary` | 关闭当前二进制分析目标并释放引擎资源。 | REA | 请用 `rea` 的 `close_binary` 关闭本对话当前打开的测试二进制，并报告关闭结果。 |
| 57 | `binary_overview` | 获取当前二进制的结构概览。 | REA | 请用 `rea` 的 `binary_overview` 汇总当前打开的测试程序，告诉我后端已识别多少个函数和字符串。 |
| 58 | `list_architectures` | 列出目标文件包含的处理器架构。 | REA | 请用 `rea` 的 `list_architectures` 检查当前打开的通用 Mach-O 测试文件，列出其中包含的处理器架构。 |
| 59 | `list_documents` | 列出分析后端可见的文档。 | REA | 请用 `rea` 的 `list_documents` 列出当前分析后端可见的文档，并告诉我哪些对应刚打开的测试程序。 |
| 60 | `list_segments` | 列出当前二进制的内存段。 | REA | 请用 `rea` 的 `list_segments` 列出当前测试程序的内存段名称以及各段的起止地址。 |
| 61 | `list_procedures` | 列出后端已识别的函数。 | REA | 请用 `rea` 的 `list_procedures` 列出当前测试程序中已识别的函数，先展示前十个名称和地址。 |
| 62 | `search_procedures` | 按条件搜索已识别的函数。 | REA | 请用 `rea` 的 `search_procedures` 在当前测试程序中按字面、不区分大小写搜索 main，列出匹配的函数。 |
| 63 | `list_names` | 列出已命名的地址和符号。 | REA | 请用 `rea` 的 `list_names` 列出当前测试程序的已命名符号，先展示十组地址和名称。 |
| 64 | `address_name` | 查询一个地址对应的符号名。 | REA | 请用 `rea` 的 `address_name` 查询上一条函数列表中第一个函数的起始地址，告诉我它的符号名。 |
| 65 | `inspect_address_context` | 查看指定地址的名称、所属函数及后端可提供的上下文。 | REA | 请用 `rea` 的 `inspect_address_context` 检查上一条函数列表中第一个函数的起始地址，给出所属函数和可读取的注释。 |
| 66 | `set_address_name` | 在分析会话中修改一个地址的符号名。 | REA | 请用 `rea` 的 `set_address_name` 将我选中的测试函数起始地址重命名为 demo_entry，并告诉我改动的地址。 |
| 67 | `set_addresses_names` | 在分析会话中批量修改地址的符号名。 | REA | 请用 `rea` 的 `set_addresses_names` 将我依次选中的两个不同测试函数地址分别命名为 demo_load 和 demo_save。 |
| 68 | `list_cutter_sessions` | 列出本机可发现的 Cutter 桥接会话。 | REA | 请用 `rea` 的 `list_cutter_sessions` 列出这台 Mac 当前可发现的 Cutter 桥接会话，没有会话就报告空列表。 |
| 69 | `inspect_native_exports` | 读取 PE 导出项或 ELF 动态导出符号。 | REA | 请用 `rea` 的 `inspect_native_exports` 从我提供的 libdemo.so 列出已定义的动态导出符号，先显示前十个。 |
| 70 | `inspect_binary_hardening` | 查看 ELF、PE 或 Mach-O 声明的二进制安全加固特性。 | REA | 请用 `rea` 的 `inspect_binary_hardening` 检查我提供的 demo ELF 文件，列出它声明的 PIE、NX 和 RELRO 状态。 |
| 71 | `inspect_byte_entropy` | 计算文件整体或指定区域的字节熵，观察字节分布。 | REA | 请用 `rea` 的 `inspect_byte_entropy` 计算我提供的 sample.bin 的整体字节熵，并按 4096 字节分块展示分布。 |

<a name="group-7"></a>

## Windows、Linux 与设备文件（9 项）

| 序号 | 工具名 | 中文用途 | 来源 | 中文调用示例 |
|---:|---|---|---|---|
| 72 | `inspect_pe_imports` | 列出 Windows PE 导入的 DLL 及其函数。 | REA | 请用 `rea` 的 `inspect_pe_imports` 读取我提供的 demo.exe，按 DLL 分组列出它导入的函数。 |
| 73 | `inspect_pe_resources` | 查看 PE 资源树中的类型、名称、语言和数据范围。 | REA | 请用 `rea` 的 `inspect_pe_resources` 查看我提供的 demo.exe 的资源树，列出资源类型和对应的语言编号。 |
| 74 | `inspect_pe_certificates` | 查看 PE 证书表及其中记录的签名者和算法。 | REA | 请用 `rea` 的 `inspect_pe_certificates` 读取我提供的 demo.exe 的证书表，列出其中记录的签名者和摘要算法。 |
| 75 | `inspect_windows_shortcut` | 读取 Windows 快捷方式记录的路径、参数和工作目录。 | REA | 请用 `rea` 的 `inspect_windows_shortcut` 静态读取我提供的 Demo.lnk，告诉我它记录的目标路径和工作目录。 |
| 76 | `inspect_ntfs_journal` | 检查 NTFS 变更日志记录。 | REA | 请用 `rea` 的 `inspect_ntfs_journal` 使用我提供的同一卷的 MFT 和 USN 日志文件，列出最先读到的十条变更记录。 |
| 77 | `inspect_elf_notes` | 读取 ELF 注记的类型、所有者及数据范围。 | REA | 请用 `rea` 的 `inspect_elf_notes` 读取我提供的 demo ELF 文件，列出注记的所有者和类型，并标出可识别的构建 ID。 |
| 78 | `inspect_kernel_build_config` | 从 Linux 内核映像读取构建标识及嵌入的内核配置。 | REA | 请用 `rea` 的 `inspect_kernel_build_config` 查看我提供的 vmlinux 中嵌入的配置，告诉我 CONFIG_SMP 的记录值。 |
| 79 | `inspect_kernel_module` | 查看 Linux 内核模块的元数据、符号和签名区信息。 | REA | 请用 `rea` 的 `inspect_kernel_module` 从我提供的 demo.ko 中读取模块名称、许可证以及声明的依赖。 |
| 80 | `inspect_devicetree` | 解析扁平设备树，查看硬件节点、属性和内存保留区。 | REA | 请用 `rea` 的 `inspect_devicetree` 读取我提供的 board.dtb，列出根节点下的设备节点及其 compatible 属性。 |

<a name="group-8"></a>

## 编程语言、托管代码与计算模型（15 项）

| 序号 | 工具名 | 中文用途 | 来源 | 中文调用示例 |
|---:|---|---|---|---|
| 81 | `inspect_go_binary` | 从 Go 二进制读取编译器、模块、依赖及构建参数。 | REA | 请用 `rea` 的 `inspect_go_binary` 检查我提供的 Go 测试程序，列出编译器版本、主模块和依赖模块。 |
| 82 | `inspect_rust_binary` | 从含 cargo-auditable 元数据的 Rust 二进制读取依赖。 | REA | 请用 `rea` 的 `inspect_rust_binary` 从我提供的含 cargo-auditable 元数据的 Rust 测试程序中列出依赖包及版本。 |
| 83 | `inspect_erlang_beam` | 解析 Erlang BEAM 文件中的数据块、原子和导入导出项。 | REA | 请用 `rea` 的 `inspect_erlang_beam` 读取我提供的 demo.beam，列出导出函数的名称及参数个数。 |
| 84 | `inspect_python_pyc` | 静态读取 CPython 字节码文件头、代码对象及常量摘要。 | REA | 请用 `rea` 的 `inspect_python_pyc` 查看我提供的 demo.pyc，告诉我其对应的 CPython 版本及记录的代码对象名称。 |
| 85 | `inspect_v8_code_cache` | 查看 V8 或 bytenode 代码缓存的文件头和结构。 | REA | 请用 `rea` 的 `inspect_v8_code_cache` 读取我提供的 demo.jsc，列出可识别的 V8 缓存文件头字段。 |
| 86 | `inspect_managed_artifact` | 查看 .NET 托管程序集的标识与 PE/CLI 元数据。 | REA | 请用 `rea` 的 `inspect_managed_artifact` 读取我提供的 Demo.dll，告诉我程序集名称、版本和托管元数据概况。 |
| 87 | `compare_managed_members` | 对比两组已有的托管成员记录，识别对应成员及差异。 | REA | 请用 `rea` 的 `compare_managed_members` 比较我提供的新旧两份 REA 托管成员证据，列出能够匹配的成员及其签名变化。 |
| 88 | `inspect_managed_native_boundaries` | 查看 .NET 程序集中的 P/Invoke 等原生调用声明。 | REA | 请用 `rea` 的 `inspect_managed_native_boundaries` 从我提供的 Demo.dll 列出 P/Invoke 声明及各自引用的原生库。 |
| 89 | `verify_managed_native_boundaries` | 将托管调用声明与已有的原生导出或函数记录核对。 | REA | 请用 `rea` 的 `verify_managed_native_boundaries` 用本对话的 P/Invoke 声明证据和对应 DLL 的原生导出证据，核对哪些入口名能匹配。 |
| 90 | `project_managed_application_graph` | 将托管程序集、成员及原生调用关系整理为应用关系图。 | REA | 请用 `rea` 的 `project_managed_application_graph` 使用我提供的 REA 托管成员证据生成 .NET 应用关系图，列出其中可识别的类型与成员。 |
| 91 | `inspect_il2cpp_metadata` | 查看 Unity IL2CPP 元数据表及可关联的原生方法。 | REA | 请用 `rea` 的 `inspect_il2cpp_metadata` 读取我提供的 Unity 测试项目的 global-metadata.dat，列出元数据版本和可识别的表。 |
| 92 | `inspect_wasm_artifact` | 使用 WABT 验证 WebAssembly 模块并查看段、导入导出和 WAT 表示。 | REA | 请用 `rea` 的 `inspect_wasm_artifact` 验证我提供的 demo.wasm，列出模块导入和导出的名称。 |
| 93 | `compare_wasm_interfaces` | 对比两个 WebAssembly 模块导入导出项的名称、种类和签名。 | REA | 请用 `rea` 的 `compare_wasm_interfaces` 比较本对话中两份 WASM 模块检查结果，列出新增、移除或签名变化的导出项。 |
| 94 | `inspect_gpu_code_objects` | 查看 CUDA 或 HIP 代码对象及内核条目。 | REA | 请用 `rea` 的 `inspect_gpu_code_objects` 盘点我提供的 demo.cubin，列出可识别的 GPU 目标架构。 |
| 95 | `inspect_model_artifact` | 读取 GGUF 或 safetensors 模型的元数据和张量声明。 | REA | 请用 `rea` 的 `inspect_model_artifact` 读取我提供的 demo.safetensors，列出每个张量的名称、数据类型和形状。 |

<a name="group-9"></a>

## 文件、应用包与数据库（5 项）

| 序号 | 工具名 | 中文用途 | 来源 | 中文调用示例 |
|---:|---|---|---|---|
| 96 | `inspect_artifact` | 识别本地文件或应用包，查看支持格式的内容清单。 | REA | 请用 `rea` 的 `inspect_artifact` 检查当前已打开的 demo.zip，列出内部文件的路径和条目标识。 |
| 97 | `extract_artifact` | 从已打开的归档中将全部或选定文件解包到本地目录。 | REA | 请用 `rea` 的 `extract_artifact` 按上一条清单中 README.txt 的条目标识，只把这个文件解包到工作区新目录 demo-extract。 |
| 98 | `inspect_desktop_application` | 从桌面应用目录识别可能使用的框架和运行时。 | REA | 请用 `rea` 的 `inspect_desktop_application` 检查我提供的桌面应用安装目录，根据文件和元数据列出可能使用的运行时。 |
| 99 | `audit_release_exposure` | 检查已发布应用包中仍可被静态读取的信息。 | REA | 请用 `rea` 的 `audit_release_exposure` 检查我自己的 Demo.app 发布包，列出可从成品静态读取的信息及对应文件。 |
| 100 | `inspect_sqlite_database` | 读取 SQLite 快照的表结构，可查看指定列和记录。 | REA | 请用 `rea` 的 `inspect_sqlite_database` 从我提供的 demo.sqlite 快照的 products 表中读取前五行，只显示 id 和 name 两列。 |

<a name="group-10"></a>

## 证据、版本差异与重建验证（17 项）

本机实测中，证据包的导入、导出和对比使用临时会话的空包；进程对比和静态与运行时关联使用离线合成记录；环境包导出使用手写 HAR。

| 序号 | 工具名 | 中文用途 | 来源 | 中文调用示例 |
|---:|---|---|---|---|
| 101 | `get_evidence_bundle` | 读取当前会话保留的分析证据及待解问题。 | REA | 请用 `rea` 的 `get_evidence_bundle` 以摘要列出当前会话保留的证据，给出记录 ID 和产生记录的工具。 |
| 102 | `export_evidence_bundle` | 把当前会话的证据包写入本地文件。 | REA | 请用 `rea` 的 `export_evidence_bundle` 把本次测试会话的证据包保存为工作区中新文件 demo-evidence.json。 |
| 103 | `import_evidence_bundle` | 校验证据包后，将其中的记录合并到当前会话。 | REA | 请用 `rea` 的 `import_evidence_bundle` 校验我提供的 demo-evidence.json，并把通过校验的记录导入当前测试会话。 |
| 104 | `compare_bundles` | 比较两份分析证据包。 | REA | 请用 `rea` 的 `compare_bundles` 对比我提供的 before-evidence.json 和 after-evidence.json，概括证据记录的差异。 |
| 105 | `compare_artifacts` | 比较两份分析产物记录中的差异。 | REA | 请用 `rea` 的 `compare_artifacts` 比较本对话中旧版和新版安装包的两份文件清单证据，列出新增和内容变化的文件。 |
| 106 | `compare_process_captures` | 对比两份已有的进程观测记录。 | REA | 请用 `rea` 的 `compare_process_captures` 对比我提供的同一测试命令前后两次的 REA 进程记录，告诉我终端输出有什么变化。 |
| 107 | `find_changed_behavior` | 汇总已有的进程、产物和函数比较结果，定位行为变化。 | REA | 请用 `rea` 的 `find_changed_behavior` 汇总本对话中已有的产物和进程比较证据，指出哪些行为有可核实的变化。 |
| 108 | `correlate_static_and_runtime` | 用已有的静态和运行时比较结果核对指定的关联假设。 | REA | 请用 `rea` 的 `correlate_static_and_runtime` 使用本对话的函数比较和进程比较证据，按旧版对应旧版、新版对应新版，核对该函数的变化是否伴随终端输出变化。 |
| 109 | `build_reconstruction_obligation_ledger` | 整理重建工作需要验证的事项及相应证据。 | REA | 请用 `rea` 的 `build_reconstruction_obligation_ledger` 根据我提供的 REA 证据包、已审阅事项和重建清单，列出仍需验证的事项。 |
| 110 | `evaluate_reconstruction_coverage` | 检查指定范围的重建验证覆盖了哪些要求、还缺哪些证据。 | REA | 请用 `rea` 的 `evaluate_reconstruction_coverage` 使用我提供的覆盖评估输入，检查 replacement.cli 这个边界还有哪些要求缺少验证证据。 |
| 111 | `verify_reconstruction` | 按明确列出的行为和结构要求核验重建结果。 | REA | 请用 `rea` 的 `verify_reconstruction` 按我提供的重建规格和本会话的证据，核验两版测试命令的终端输出是否满足规格中的一致性要求。 |
| 112 | `record_unknown` | 将尚未解决的问题记入调查记录。 | REA | 请用 `rea` 的 `record_unknown` 在“离线输出”领域登记中等严重度问题“相同输入是否生成相同摘要”，以受控重放的实测结果为结案依据，暂不指定环境、关联记录或后续探针，并返回问题 ID。 |
| 113 | `list_unknowns` | 按状态、严重程度或领域列出待解问题。 | REA | 请用 `rea` 的 `list_unknowns` 列出当前调查中严重度为中等的待解问题，最多显示十条。 |
| 114 | `update_unknown` | 更新已记录问题的内容或处理状态。 | REA | 请用 `rea` 的 `update_unknown` 使用上一条问题的 ID 和当前修订号，将该问题的处理状态更新为调查中。 |
| 115 | `verify_unknown_resolution` | 对照证据核验某个问题是否满足结案条件。 | REA | 请用 `rea` 的 `verify_unknown_resolution` 根据我选中的问题 ID 和当前证据，说明它是否满足结案条件。 |
| 116 | `export_environment_bundle` | 将已保存的浏览器场景或 HAR 证据导出为本地环境包。 | REA | 请用 `rea` 的 `export_environment_bundle` 用本对话中合成 HAR 的分析证据，把测试环境包导出到工作区新目录 demo-environment。 |
| 117 | `reset_investigation` | 清空当前调查保留的证据和问题历史。 | REA | 请用 `rea` 的 `reset_investigation` 将当前临时测试调查的证据保存到工作区新文件 before-reset.json，再清空这次调查的证据和问题历史。 |

<a name="group-11"></a>

## 工作指南、设置与结果浏览（6 项）

| 序号 | 工具名 | 中文用途 | 来源 | 中文调用示例 |
|---:|---|---|---|---|
| 118 | `guided_workflows` | 浏览 REA 自带的工作流程及操作指南。 | REA | 请用 `rea` 的 `guided_workflows` 列出 REA 内置的工作流程，并指出哪一个适合初次检查应用包。 |
| 119 | `search_guidance` | 按关键词查找已安装的 REA 指南章节。 | REA | 请用 `rea` 的 `search_guidance` 在已安装的指南中搜索 JavaScript module，给出最相关的三个章节及定位信息。 |
| 120 | `read_guidance_section` | 读取选定的指南章节。 | REA | 请用 `rea` 的 `read_guidance_section` 用上一条指南搜索结果中第一项的定位信息读取该节，并概括操作步骤。 |
| 121 | `inspect_analysis_settings` | 查看分析的大小限制、超时和工作进程内存设置。 | REA | 请用 `rea` 的 `inspect_analysis_settings` 查看 asar.max_header_bytes 的当前值、允许范围和生效时机。 |
| 122 | `update_analysis_settings` | 调整或重置后续分析任务使用的运行时设置。 | REA | 请用 `rea` 的 `update_analysis_settings` 仅将本次 REA 服务中的 asar.max_header_bytes 重置为启动时的值，并报告结果。 |
| 123 | `inspect_analysis_view` | 按视图读取已保留的分析结果，支持分段浏览。 | REA | 请用 `rea` 的 `inspect_analysis_view` 使用上一条 Web 应用分析摘要返回的父证据 ID，从 endpoints 集合的第一项起读取十条接口记录。 |
