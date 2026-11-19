# Codex 对话可用工具中文清单

本机累计实测 **123 项**，其中 **120 项来自 REA 6.9.0**，**3 项由 Mac 的本地 Wireshark 服务替代**。仅列入已通过 Codex 对话的工具连接得到有效返回的项目。不同工具使用各自支持的样例、后端或会话；部分验证使用空证据包、空设备列表或合成记录。

在对话中说出服务名、工具名和要处理的对象即可。例如：“用 mac_pcap 的 inspect_packet_capture 读取这个抓包里前 10 帧的帧号和长度。”表中的 **Mac 替代** 均调用 `mac_pcap`；其余各项调用 `rea`。

每行的“中文调用示例”都可以复制到 Codex。示例文件名可替换为自己的本地文件路径；抓包示例可使用[随附的两帧样例](./mac-pcap/两帧样例.pcap)。提到“当前”“上一条”或“本对话”的示例，请在相应的目标已打开或前一步结果就绪时使用。

**练习入口**　[下载测试样例包](./测试样例.zip) · [50 条文件示例和 58 条会话准备指令](./Codex样例与会话准备.md)。各行工具名后的链接可直达本项。

[15 条直接用示例的最终指令和全新对话实测](./15条直接用示例全新对话实测.md)

## 对话实测结果（2026-11-20）

逐句发送示例并核对 Codex 实际发起的 MCP 调用。全部 **123 条**都在本机得到与示例对应的结果，其中 **15 条直接用**，**50 条先备文件或材料**，**58 条先备会话或前序结果**。本轮调整了 12 句，清单采用的每个版本都已通过对话复测。[逐条调用记录](./Codex中文示例逐条实测.json)

| 使用条件 | 复制示例前需要做什么 |
|---|---|
| 直接用 | 在已配置的这台 Mac 上打开 Codex 即可。查询默认会话允许返回空列表；导出空包需要可写的工作目录。 |
| 先备文件或材料 | 提供示例需要的本地文件、目录或结构化材料。表中给出具体类型，示意文件名可替换为自己的路径。 |
| 先备会话或前序结果 | 先打开目标、连接本机测试页面，或准备上一步返回的对象和证据 ID。引用保留证据时，在产生或已导入该证据的同一 REA 会话里继续。 |

“本次返回”记录了样例上的实际结果，包括空列表、仅部分可验证的结论和未命中项。重命名、保存、导入及重置均在隔离测试会话或临时目录执行。

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

| 序号 | 工具名 | 中文用途 | 来源 | 使用条件 | 中文调用示例 | 本次返回 |
|---:|---|---|---|---|---|---|
| 1 | `inspect_packet_fields` | 按字段名前缀查 Wireshark 字段及英文名称，例如查询 frame.len。 | **Mac 替代** | **直接用** · 字段前缀即可 | 请用 `mac_pcap` 的 `inspect_packet_fields` 查找以 frame.len 开头的 Wireshark 字段，告诉我哪个字段表示帧长。 | frame.len 的标签是 Frame Length。 |
| 2 | `inspect_packet_capture` [〔样例〕](./Codex样例与会话准备.md#item-2) | 从离线抓包逐帧读取指定字段，可按 Wireshark 显示过滤器筛选。 | **Mac 替代** | **先备文件或材料** · 本地未压缩抓包 | 请用 `mac_pcap` 的 `inspect_packet_capture` 读取我提供的《两帧样例.pcap》，按帧号列出 frame.number 和 frame.len。 | 两帧分别为 60、74 字节，帧号为 1、2。 |
| 3 | `inspect_pcap_capture` [〔样例〕](./Codex样例与会话准备.md#item-3) | 汇总离线抓包的格式、链路类型、包数、文件大小、线上字节数和时长。 | **Mac 替代** | **先备文件或材料** · 本地未压缩抓包 | 请用 `mac_pcap` 的 `inspect_pcap_capture` 汇总我提供的《两帧样例.pcap》，告诉我包数、线上字节总数和持续时间。 | 2 个包，线上共 134 字节，时长 1 秒。 |
| 4 | `inspect_pcap_client` | 检查本机 TShark 和 capinfos 的路径及版本。 | REA | **直接用** · 本机已配置 Wireshark | 请用 `rea` 的 `inspect_pcap_client` 检查这台 Mac 上 TShark 和 capinfos 的实际路径和版本。 | TShark 和 capinfos 均报告 4.6.10，并给出实际路径。 |
| 5 | `inspect_web_network_capture` [〔样例〕](./Codex样例与会话准备.md#item-5) | 读取已保存的 HAR 等网络记录，查看其中的请求和事件。 | REA | **先备文件或材料** · HAR 文件 | 请用 `rea` 的 `inspect_web_network_capture` 读取我提供的 demo.har，按记录顺序列出前五个请求的方法、路径和响应状态码。 | 读到 1 条 GET /demo/report，状态码 200。 |

<a name="group-2"></a>

## 网页、浏览器与 Electron（10 项）

| 序号 | 工具名 | 中文用途 | 来源 | 使用条件 | 中文调用示例 | 本次返回 |
|---:|---|---|---|---|---|---|
| 6 | `inspect_web_page` [〔准备〕](./Codex样例与会话准备.md#item-6) | 查看已连接浏览器页面的结构与资源。 | REA | **先备会话或前序结果** · 已连接的本机 CDP 页面 | 请用 `rea` 的 `inspect_web_page` 检查我通过本机 CDP 连接并指定的测试页，告诉我页面标题和加载了哪些脚本。 | 读到测试页标题和 1 段内联脚本。 |
| 7 | `inspect_web_event_listeners` [〔准备〕](./Codex样例与会话准备.md#item-7) | 查看指定页面元素直接注册的事件监听器及回调来源。 | REA | **先备会话或前序结果** · CDP 页面及存在的 CSS 选择器 | 请用 `rea` 的 `inspect_web_event_listeners` 查看指定 CDP 测试页上 #submit 按钮直接注册的监听器，列出事件类型及可定位的回调脚本。 | 按钮有 1 个 click 监听器，定位到内联脚本。 |
| 8 | `capture_web_screenshot` [〔准备〕](./Codex样例与会话准备.md#item-8) | 截取当前网页可见区域，返回 PNG 图像。 | REA | **先备会话或前序结果** · CDP 页面及目标 ID | 请用 `rea` 的 `capture_web_screenshot` 为我指定的本机 CDP 测试页截一张当前可见区域的 PNG。 | 返回 8,820 字节的可见区域 PNG。 |
| 9 | `compare_web_screenshots` [〔准备〕](./Codex样例与会话准备.md#item-9) | 逐像素比较两张网页截图，统计变化比例和通道差异。 | REA | **先备会话或前序结果** · 两份带校验信息的 REA 截图对象 | 请用 `rea` 的 `compare_web_screenshots` 比较本对话中先后取得的两份 REA 网页截图，给出发生变化的像素占比。 | 用两份单像素合成截图比较，变化像素为 0%。 |
| 10 | `observe_web_session` [〔准备〕](./Codex样例与会话准备.md#item-10) | 在指定时段记录用户操作网页时发生的浏览器事件。 | REA | **先备会话或前序结果** · CDP 页面及观测时段 | 请用 `rea` 的 `observe_web_session` 在我操作指定的本机 CDP 测试页时观察 10 秒，按顺序概括记录到的页面事件。 | 观察满 10 秒，静置期间记录到 0 条事件。 |
| 11 | `compare_web_captures` [〔准备〕](./Codex样例与会话准备.md#item-11) | 比较两次页面检查或两段已录制的浏览器场景。 | REA | **先备会话或前序结果** · 两份同类型的完整浏览器记录 | 请用 `rea` 的 `compare_web_captures` 比较我提供的改版前后两份同类 REA 浏览器场景记录，列出有变化的页面资源。 | 测试脚本 main.js 的常量由 1 改为 2。 |
| 12 | `discover_webmcp_tools` [〔准备〕](./Codex样例与会话准备.md#item-12) | 列出网页声明的 WebMCP 工具及输入参数结构。 | REA | **先备会话或前序结果** · 支持 WebMCP 的 CDP 页面 | 请用 `rea` 的 `discover_webmcp_tools` 查看我指定的本机 CDP 测试页声明了哪些 WebMCP 工具，给出名称和参数。 | 完成发现；此测试页声明了 0 个工具。 |
| 13 | `inspect_playwright_trace` [〔样例〕](./Codex样例与会话准备.md#item-13) | 检查已保存的 Playwright 跟踪记录。 | REA | **先备文件或材料** · Playwright 跟踪包 | 请用 `rea` 的 `inspect_playwright_trace` 读取我提供的 trace.zip，按记录顺序列出前十条网络事件。 | 从 trace.zip 读到 3 条网络事件。 |
| 14 | `inspect_electron_page` [〔准备〕](./Codex样例与会话准备.md#item-14) | 查看已连接的 Electron 本地文件页面及其框架信息。 | REA | **先备会话或前序结果** · Electron 本地文件页、CDP 端点及目标 ID | 请用 `rea` 的 `inspect_electron_page` 使用我提供的本机 CDP 端点和目标 ID，查看 Electron 测试应用中本地文件页的主框架 URL。 | 独立 Electron 测试页返回 index.html 的 file URL。 |
| 15 | `inspect_electron_fuses` [〔样例〕](./Codex样例与会话准备.md#item-15) | 读取 Electron 安装包中编译固化的功能开关。 | REA | **先备文件或材料** · Electron 应用包或框架二进制 | 请用 `rea` 的 `inspect_electron_fuses` 检查我提供的 Demo.app，列出其中 Electron 功能开关的名称和当前值。 | 在 arm64 测试应用中读到 9 个开关，5 开、4 关。 |

<a name="group-3"></a>

## JavaScript、源码映射与 API（13 项）

| 序号 | 工具名 | 中文用途 | 来源 | 使用条件 | 中文调用示例 | 本次返回 |
|---:|---|---|---|---|---|---|
| 16 | `analyze_javascript_application` [〔样例〕](./Codex样例与会话准备.md#item-16) | 静态分析 JavaScript 应用，生成模块、依赖等关系图。 | REA | **先备文件或材料** · JavaScript 应用包或目录 | 请用 `rea` 的 `analyze_javascript_application` 分析我提供的 app.asar，列出入口模块及其直接导入的模块。 | 识别入口 renderer.js 及其直接依赖 profile.js。 |
| 17 | `trace_application_feature` [〔准备〕](./Codex样例与会话准备.md#item-17) | 从指定起点沿 JavaScript 应用关系图追踪一项功能。 | REA | **先备会话或前序结果** · JavaScript 应用图及真实起点 | 请用 `rea` 的 `trace_application_feature` 在刚生成的 JavaScript 应用图中，以 renderer.js 模块为起点追踪它关联的功能。 | 从 renderer.js 追踪到 6 个节点、6 条关系。 |
| 18 | `trace_javascript_semantics` [〔准备〕](./Codex样例与会话准备.md#item-18) | 追踪静态数据流、直接调用、返回值和闭包关系。 | REA | **先备会话或前序结果** · 应用图及选中的语义节点 | 请用 `rea` 的 `trace_javascript_semantics` 使用我选中的语义节点 ID，在本对话的 JavaScript 应用图中向后追溯它的值来自哪里。 | 追溯到 getProfile 返回点；样例没有更早的来源节点。 |
| 19 | `trace_web_module_imports` [〔样例〕](./Codex样例与会话准备.md#item-19) | 从已导出脚本追踪 ES 模块导入和再导出的来源。 | REA | **先备文件或材料** · 已导出的脚本及 manifest.json | 请用 `rea` 的 `trace_web_module_imports` 读取我提供的脚本导出清单 manifest.json，列出编号 0 的脚本导入了哪些模块。 | 解析了编号 0 的 main.js，原生 ES 导入为 0 项。 |
| 20 | `trace_web_source_location` [〔样例〕](./Codex样例与会话准备.md#item-20) | 利用本地 source map 将生成脚本的行列位置映射回源码。 | REA | **先备文件或材料** · 导出清单、映射文件及其原始 URL | 请用 `rea` 的 `trace_web_source_location` 用我提供的脚本清单、配套 source map 本地路径和原始 URL，将编号 0 的脚本第 1 行、第 0 列映射回源码。 | main.js 的第 1 行第 0 列映射到 main.ts 的同一位置。 |
| 21 | `export_web_scripts` [〔样例〕](./Codex样例与会话准备.md#item-21) | 将网页记录中已保存的 JavaScript 导出为脚本文件和校验清单。 | REA | **先备文件或材料** · 已保存的网页记录及新输出目录 | 请用 `rea` 的 `export_web_scripts` 从我提供的页面检查记录 capture.json 导出已保存的脚本，将脚本和清单写入工作区新目录 scripts-export。 | 导出 22 字节的 main.js 和 manifest.json。 |
| 22 | `compare_source_to_bundle` [〔准备〕](./Codex样例与会话准备.md#item-22) | 对照历史源码和打包产物，识别保留、变更及无法匹配的部分。 | REA | **先备会话或前序结果** · 应用图及配套的历史源码图 | 请用 `rea` 的 `compare_source_to_bundle` 将我提供的历史源码图 HistoricalSourceGraph 与本对话的打包应用图比对，列出修改过的模块。 | 生成比对结果；样例中的两个历史模块均未匹配，修改状态未知。 |
| 23 | `compare_application_versions` [〔准备〕](./Codex样例与会话准备.md#item-23) | 对比两个版本的 JavaScript 应用关系图，列出新增、删除和变化。 | REA | **先备会话或前序结果** · 新旧两份完整应用图或摘要中的父证据 ID | 请用 `rea` 的 `compare_application_versions` 使用本会话中新旧两份 JavaScript 分析摘要各自的 parent_evidence_id 对比应用图，分别列出新增和删除的模块。 | 两版模块节点新增 2 个、删除 2 个；按节点身份统计。 |
| 24 | `compare_javascript_export_shapes` [〔准备〕](./Codex样例与会话准备.md#item-24) | 比较两个 JavaScript 模块指定导出项的静态返回属性结构。 | REA | **先备会话或前序结果** · 两份应用图及实际模块名、导出名 | 请用 `rea` 的 `compare_javascript_export_shapes` 使用新旧 JavaScript 分析摘要各自的 parent_evidence_id，比较两版 profile.js 中 getProfile 的静态返回属性。 | getProfile 的返回值新增 count，保留 name。 |
| 25 | `observe_javascript_runtime` [〔准备〕](./Codex样例与会话准备.md#item-25) | 查看本机 Node 或 Electron 运行时已载入的脚本与执行上下文。 | REA | **先备会话或前序结果** · 本机 V8 Inspector 端点及目标 ID | 请用 `rea` 的 `observe_javascript_runtime` 使用我提供的本机 V8 Inspector 端点和目标 ID，列出 Node 测试进程已载入的脚本。 | 观察到 Node 测试进程载入 83 个脚本。 |
| 26 | `reconcile_javascript_runtime` [〔准备〕](./Codex样例与会话准备.md#item-26) | 对照 JavaScript 静态关系图与已有运行时观测记录。 | REA | **先备会话或前序结果** · 静态应用图及 V8 观测证据 | 请用 `rea` 的 `reconcile_javascript_runtime` 对齐本对话的 JavaScript 静态应用图和已有的 V8 观测记录，列出两边都能确认的脚本。 | 完成对齐；83 个运行时脚本中可确认与此静态图对应的有 0 个。 |
| 27 | `compare_static_and_observed_endpoints` [〔准备〕](./Codex样例与会话准备.md#item-27) | 将代码中声明的接口与 HAR 实际记录的请求配对。 | REA | **先备会话或前序结果** · 应用图、HAR 分析证据及应用来源 | 请用 `rea` 的 `compare_static_and_observed_endpoints` 核对本对话的应用图与同一测试应用的 HAR 分析结果，列出代码声明且抓包中出现过的接口。 | 精确匹配 /demo/report；GET 由 HAR 确认。 |
| 28 | `inspect_api_contract` [〔样例〕](./Codex样例与会话准备.md#item-28) | 从本地 OpenAPI JSON 或 GraphQL SDL 读取接口声明。 | REA | **先备文件或材料** · OpenAPI 或 GraphQL 声明文件 | 请用 `rea` 的 `inspect_api_contract` 读取我提供的 openapi.json，按路径列出声明的 HTTP 方法。 | 从本地 OpenAPI 文件读到 GET /books。 |

<a name="group-4"></a>

## Android、ADB、Flutter 与鸿蒙（12 项）

| 序号 | 工具名 | 中文用途 | 来源 | 使用条件 | 中文调用示例 | 本次返回 |
|---:|---|---|---|---|---|---|
| 29 | `inspect_android_package` [〔样例〕](./Codex样例与会话准备.md#item-29) | 读取 APK 的包名、SDK、权限、组件以及类和资源数量。 | REA | **先备文件或材料** · Android APK | 请用 `rea` 的 `inspect_android_package` 查看我提供的 demo.apk，列出包名、目标 SDK 和声明的权限。 | 读到包名 de.rhab.helloworld、目标 SDK 25。 |
| 30 | `inspect_apk_signature` [〔样例〕](./Codex样例与会话准备.md#item-30) | 查看 APK 声明的签名方案、签名者和证书指纹。 | REA | **先备文件或材料** · 已签名 APK | 请用 `rea` 的 `inspect_apk_signature` 读取我提供的 demo.apk，列出检测到的签名方案和签名证书指纹。 | 识别到 v1、v2 签名及相同的证书指纹。 |
| 31 | `search_android_classes` [〔样例〕](./Codex样例与会话准备.md#item-31) | 在 APK 的顶层类名中按子串搜索。 | REA | **先备文件或材料** · APK 及搜索字串 | 请用 `rea` 的 `search_android_classes` 在我提供的 demo.apk 中搜索名称含 Activity 的类，列出完整类名。 | 找到 24 个名称含 Activity 的类。 |
| 32 | `inspect_android_class` [〔样例〕](./Codex样例与会话准备.md#item-32) | 查看指定 Android 类的方法、字段、内部类和 DEX 类型信息。 | REA | **先备文件或材料** · APK 及真实完整类名 | 请用 `rea` 的 `inspect_android_class` 在我提供的 APK 里，读取刚才搜索结果中选定的完整类名，列出该类声明的字段和方法。 | MainActivity 有 4 个方法，声明的字段为 0 个。 |
| 33 | `inspect_apktool_client` | 检查本机 Apktool 的启动命令和版本。 | REA | **直接用** · 本机已配置 Apktool | 请用 `rea` 的 `inspect_apktool_client` 检查这台 Mac 实际使用的 Apktool 启动命令和版本。 | 读到启动命令，版本为 3.0.3。 |
| 34 | `decode_android_resources` [〔样例〕](./Codex样例与会话准备.md#item-34) | 解码 APK 的清单、字符串和多语言资源。 | REA | **先备文件或材料** · 含资源的 APK | 请用 `rea` 的 `decode_android_resources` 解码我提供的 demo.apk，列出实际包含的语言资源，并从每种语言中举一个字符串示例。 | 识别 81 个限定语言资源表和 1 个默认表，返回了字符串。 |
| 35 | `inspect_adb_client` | 查看本机 ADB 客户端的位置及版本。 | REA | **直接用** · 本机已配置 ADB | 请用 `rea` 的 `inspect_adb_client` 告诉我本机 ADB 客户端的安装位置和版本。 | 读到客户端路径及版本 37.0.1。 |
| 36 | `list_adb_devices` | 列出 ADB 报告的设备及连接状态，空列表也是有效结果。 | REA | **直接用** · 本机 ADB 设备列表 | 请用 `rea` 的 `list_adb_devices` 只列出 ADB 当前可见的设备和连接状态，若列表为空就告诉我。 | 返回空设备列表；本次仅查客户端和列表。 |
| 37 | `project_android_application_graph` [〔准备〕](./Codex样例与会话准备.md#item-37) | 从 APK 的文件清单整理组件、文件摘要和运行时线索。 | REA | **先备会话或前序结果** · APK 的嵌套清单证据 | 请用 `rea` 的 `project_android_application_graph` 根据本对话里 demo.apk 的嵌套文件清单证据，列出组件路径及运行时线索。 | 识别到 AndroidManifest.xml；该样例没有运行时线索。 |
| 38 | `identify_flutter_build` [〔样例〕](./Codex样例与会话准备.md#item-38) | 识别 Flutter 构建的架构、Dart 快照和引擎标识。 | REA | **先备文件或材料** · Flutter APK | 请用 `rea` 的 `identify_flutter_build` 检查我提供的 Flutter 安装包 demo.apk，列出其中的 ABI 和可识别的 Dart 快照标识。 | 识别出 arm64-v8a 和 Dart 快照标识。 |
| 39 | `inspect_dart_aot` [〔样例〕](./Codex样例与会话准备.md#item-39) | 检查受支持的旧版 Android Dart AOT 快照结构。 | REA | **先备文件或材料** · 含受支持旧版 AOT 快照的 APK 及 ABI | 请用 `rea` 的 `inspect_dart_aot` 读取我提供的旧版 Flutter 测试 APK 中 arm64-v8a 的 Dart AOT 快照，概括可识别的结构。 | 识别 4 个 VM／isolate 数据或指令区域。 |
| 40 | `project_harmony_application_graph` [〔准备〕](./Codex样例与会话准备.md#item-40) | 从 HAP、HSP 或 App Pack 清单整理鸿蒙组件与子包关系。 | REA | **先备会话或前序结果** · 鸿蒙 App Pack 的嵌套清单证据 | 请用 `rea` 的 `project_harmony_application_graph` 根据本对话里 demo.app 鸿蒙 App Pack 的嵌套清单证据，列出子包名称及路径。 | 在实际 App Pack 内找到子包 modules/entry.hap。 |

<a name="group-5"></a>

## Apple 应用、Swift 与 Objective-C（13 项）

| 序号 | 工具名 | 中文用途 | 来源 | 使用条件 | 中文调用示例 | 本次返回 |
|---:|---|---|---|---|---|---|
| 41 | `project_apple_application_graph` [〔准备〕](./Codex样例与会话准备.md#item-41) | 从 IPA、应用包或磁盘映像的清单整理 Apple 应用及嵌套包关系。 | REA | **先备会话或前序结果** · IPA 等 Apple 包的嵌套清单证据 | 请用 `rea` 的 `project_apple_application_graph` 根据本对话里 Demo.ipa 的嵌套清单证据，列出主应用和内嵌扩展所在的目录。 | 定位到 Payload/Fixture.app；样例没有内嵌扩展。 |
| 42 | `open_bundle_resources` [〔样例〕](./Codex样例与会话准备.md#item-42) | 在会话中以只读方式打开 Apple 应用包资源。 | REA | **先备文件或材料** · 本地 Apple 应用包 | 请用 `rea` 的 `open_bundle_resources` 以只读方式打开我提供的 Demo.app 资源目录，告诉我当前选中了哪个应用包。 | 成功以只读资源模式选中 Demo.app。 |
| 43 | `decode_interface_builder` [〔准备〕](./Codex样例与会话准备.md#item-43) | 解码已编译的 storyboard 和 nib，列出界面对象、层级与连接。 | REA | **先备会话或前序结果** · 已打开的应用资源包及编译界面资源 | 请用 `rea` 的 `decode_interface_builder` 查看当前已打开的 Demo.app 中编译后的 storyboard，列出可识别的界面层级和控件连接。 | 识别 NSView 和名为 Demo 的 NSButton；无 outlet 或 action 连线。 |
| 44 | `inspect_asset_catalog` [〔准备〕](./Codex样例与会话准备.md#item-44) | 检查 Apple 应用的资源目录及其中的资源条目。 | REA | **先备会话或前序结果** · 应用资源会话及 Assets.car | 请用 `rea` 的 `inspect_asset_catalog` 查看当前已打开的 Demo.app 的资源目录，从第一项起列出最多十个资源条目。 | 资源目录共 276 条记录，返回了前 10 条。 |
| 45 | `inspect_keyed_archive` [〔准备〕](./Codex样例与会话准备.md#item-45) | 读取 Apple 键值归档中的对象和引用关系。 | REA | **先备会话或前序结果** · 应用资源会话及包内键值归档相对路径 | 请用 `rea` 的 `inspect_keyed_archive` 读取当前 Demo.app 中的 Contents/Resources/Model.plist 键值归档，列出根对象及其引用的类。 | 根对象为 NSArray，两个元素引用同一对象。 |
| 46 | `inspect_plist` [〔准备〕](./Codex样例与会话准备.md#item-46) | 读取 Apple 属性列表中的键、值与结构。 | REA | **先备会话或前序结果** · 应用资源会话及 Info.plist | 请用 `rea` 的 `inspect_plist` 读取当前 Demo.app 的 Contents/Info.plist，告诉我 CFBundleIdentifier 和 CFBundleVersion。 | 读到应用标识 dev.example.rea-smoke 和构建版本 1。 |
| 47 | `inspect_macho` [〔准备〕](./Codex样例与会话准备.md#item-47) | 查看 Mach-O 可执行文件或架构切片的结构信息。 | REA | **先备会话或前序结果** · 已成功打开 Mach-O 目标 | 请用 `rea` 的 `inspect_macho` 在已用 open_binary 成功打开的 Mach-O 样例中，列出切片架构和加载命令。 | 读到 arm64、x86_64 两个切片，arm64 有 16 条加载命令。 |
| 48 | `inspect_signature` [〔准备〕](./Codex样例与会话准备.md#item-48) | 查看 Mach-O 切片的签名身份、授权项和强化运行时状态。 | REA | **先备会话或前序结果** · 已成功打开 Mach-O 目标 | 请用 `rea` 的 `inspect_signature` 读取刚成功打开的 Mach-O 样例，列出它的签名身份和声明的授权项。 | arm64 切片签名标识为 demo，无授权项；x86_64 切片未签名。 |
| 49 | `inspect_apple_ips` [〔样例〕](./Codex样例与会话准备.md#item-49) | 从 Apple IPS 崩溃报告中读取异常、线程和加载映像。 | REA | **先备文件或材料** · Apple IPS 崩溃报告 | 请用 `rea` 的 `inspect_apple_ips` 读取我提供的 Demo.ips 崩溃报告，找出异常类型和触发崩溃的线程。 | 报告为 EXC_BAD_ACCESS（SIGSEGV），触发者为线程 0。 |
| 50 | `demangle_swift` [〔准备〕](./Codex样例与会话准备.md#item-50) | 将 Swift 编译符号还原为可读名称。 | REA | **先备会话或前序结果** · 已打开的 Mach-O 目标及 Swift 符号 | 请用 `rea` 的 `demangle_swift` 在已打开的 Mach-O 测试目标中，把 Swift 符号 $s4Test3fooyyF 还原成可读名称。 | 还原为 Test.foo() -> ()。 |
| 51 | `analyze_swift_types` [〔准备〕](./Codex样例与会话准备.md#item-51) | 整理二进制中的 Swift 类型信息。 | REA | **先备会话或前序结果** · 已打开的 Swift 二进制 | 请用 `rea` 的 `analyze_swift_types` 在当前打开的 Swift 测试程序里查找名称含 Account 的类。 | Swift 样例匹配到 main.AccountSample 及 6 个过程符号。 |
| 52 | `get_objc_classes` [〔准备〕](./Codex样例与会话准备.md#item-52) | 列出二进制中的 Objective-C 类信息。 | REA | **先备会话或前序结果** · 已打开的 Objective-C 二进制 | 请用 `rea` 的 `get_objc_classes` 在当前打开的测试程序中列出名称含 ViewController 的 Objective-C 类。 | Objective-C 类列表识别到 DemoViewController。 |
| 53 | `get_objc_protocols` [〔准备〕](./Codex样例与会话准备.md#item-53) | 列出二进制中的 Objective-C 协议信息。 | REA | **先备会话或前序结果** · 已打开的 Objective-C 二进制 | 请用 `rea` 的 `get_objc_protocols` 列出当前分析后端在已打开的测试程序中识别到的 Objective-C 协议；如果列表为空，就报告零项。 | 混编样例返回 0 个协议；本项只反映后端可识别的范围。 |

<a name="group-6"></a>

## 原生二进制、符号与分析会话（18 项）

| 序号 | 工具名 | 中文用途 | 来源 | 使用条件 | 中文调用示例 | 本次返回 |
|---:|---|---|---|---|---|---|
| 54 | `open_binary` [〔样例〕](./Codex样例与会话准备.md#item-54) | 打开本地二进制或分析数据库，选定分析后端。 | REA | **先备文件或材料** · 本地二进制及可用 Ghidra | 请用 `rea` 的 `open_binary` 用 Ghidra 打开我提供的 demo 原生测试程序，并报告识别到的文件格式。 | 成功打开 ARM64 Mach-O 测试程序。 |
| 55 | `binary_session` | 查看当前分析目标、后端及其可用能力。 | REA | **直接用** · 查询当前默认会话 | 请用 `rea` 的 `binary_session` 告诉我当前 REA 会话选中哪个文件、使用哪个分析后端。 | 新对话返回 open=false；打开文件后读到 Ghidra 12.1.4。 |
| 56 | `close_binary` [〔准备〕](./Codex样例与会话准备.md#item-56) | 关闭当前二进制分析目标并释放引擎资源。 | REA | **先备会话或前序结果** · 已打开的测试目标 | 请用 `rea` 的 `close_binary` 关闭本对话当前打开的测试二进制，并报告关闭结果。 | 成功关闭本轮的 demo 测试目标。 |
| 57 | `binary_overview` [〔准备〕](./Codex样例与会话准备.md#item-57) | 获取当前二进制的结构概览。 | REA | **先备会话或前序结果** · 已绑定的分析文档 | 请用 `rea` 的 `binary_overview` 汇总当前打开的测试程序，告诉我后端已识别多少个函数和字符串。 | Ghidra 报告 2 个函数、14 个字符串。 |
| 58 | `list_architectures` [〔准备〕](./Codex样例与会话准备.md#item-58) | 列出目标文件包含的处理器架构。 | REA | **先备会话或前序结果** · 已成功打开通用 Mach-O | 请用 `rea` 的 `list_architectures` 在刚成功打开的通用 Mach-O 文件中枚举架构，逐项给出工具识别的架构名。 | 返回 x86_64 和 arm64。 |
| 59 | `list_documents` [〔准备〕](./Codex样例与会话准备.md#item-59) | 列出分析后端可见的文档。 | REA | **先备会话或前序结果** · 已打开的分析后端 | 请用 `rea` 的 `list_documents` 列出当前分析后端可见的文档，并告诉我哪些对应刚打开的测试程序。 | 列出 1 个与测试程序对应的文档。 |
| 60 | `list_segments` [〔准备〕](./Codex样例与会话准备.md#item-60) | 列出当前二进制的内存段。 | REA | **先备会话或前序结果** · 已打开的二进制 | 请用 `rea` 的 `list_segments` 列出当前测试程序的内存段名称以及各段的起止地址。 | 列出 5 个内存块，区间含起始地址、不含结束地址。 |
| 61 | `list_procedures` [〔准备〕](./Codex样例与会话准备.md#item-61) | 列出后端已识别的函数。 | REA | **先备会话或前序结果** · 已打开的二进制 | 请用 `rea` 的 `list_procedures` 列出当前测试程序中已识别的函数，先展示前十个名称和地址。 | 列出 2 个函数及其入口地址。 |
| 62 | `search_procedures` [〔准备〕](./Codex样例与会话准备.md#item-62) | 按条件搜索已识别的函数。 | REA | **先备会话或前序结果** · 已打开的二进制 | 请用 `rea` 的 `search_procedures` 在当前测试程序中按字面、不区分大小写搜索 main，列出匹配的函数。 | 搜索 main 命中 1 个函数；匹配其别名 _main。 |
| 63 | `list_names` [〔准备〕](./Codex样例与会话准备.md#item-63) | 列出已命名的地址和符号。 | REA | **先备会话或前序结果** · 已打开的二进制 | 请用 `rea` 的 `list_names` 列出当前测试程序的已命名符号，先展示十组地址和名称。 | 返回 13 个已命名符号，展示前 10 组。 |
| 64 | `address_name` [〔准备〕](./Codex样例与会话准备.md#item-64) | 查询一个地址对应的符号名。 | REA | **先备会话或前序结果** · 已打开的二进制及已知函数地址 | 请用 `rea` 的 `address_name` 查询上一条函数列表中第一个函数的起始地址，告诉我它的符号名。 | 查到首个函数的名称 _demo_value。 |
| 65 | `inspect_address_context` [〔准备〕](./Codex样例与会话准备.md#item-65) | 查看指定地址的名称、所属函数及后端可提供的上下文。 | REA | **先备会话或前序结果** · 已打开的二进制及已知地址 | 请用 `rea` 的 `inspect_address_context` 检查上一条函数列表中第一个函数的起始地址，给出所属函数和可读取的注释。 | 确认所属函数；该 Ghidra 后端的注释字段不可用。 |
| 66 | `set_address_name` [〔准备〕](./Codex样例与会话准备.md#item-66) | 在分析会话中修改一个地址的符号名。 | REA | **先备会话或前序结果** · 可编辑的测试会话及选定地址 | 请用 `rea` 的 `set_address_name` 将我选中的测试函数起始地址重命名为 demo_entry，并告诉我改动的地址。 | 单个函数在测试会话中成功改名为 demo_entry。 |
| 67 | `set_addresses_names` [〔准备〕](./Codex样例与会话准备.md#item-67) | 在分析会话中批量修改地址的符号名。 | REA | **先备会话或前序结果** · 可编辑的测试会话及两个不同地址 | 请用 `rea` 的 `set_addresses_names` 将我依次选中的两个不同测试函数地址分别命名为 demo_load 和 demo_save。 | 成功将两处改名为 demo_load、demo_save。 |
| 68 | `list_cutter_sessions` | 列出本机可发现的 Cutter 桥接会话。 | REA | **直接用** · 查询本机桥接会话 | 请用 `rea` 的 `list_cutter_sessions` 列出这台 Mac 当前可发现的 Cutter 桥接会话，没有会话就报告空列表。 | 发现 0 个 Cutter 会话，正常返回空列表。 |
| 69 | `inspect_native_exports` [〔样例〕](./Codex样例与会话准备.md#item-69) | 读取 PE 导出项或 ELF 动态导出符号。 | REA | **先备文件或材料** · ELF 共享库或 PE 文件 | 请用 `rea` 的 `inspect_native_exports` 从我提供的 libdemo.so 列出已定义的动态导出符号，先显示前十个。 | 从 ELF 样例读到导出函数 demo_add。 |
| 70 | `inspect_binary_hardening` [〔样例〕](./Codex样例与会话准备.md#item-70) | 查看 ELF、PE 或 Mach-O 声明的二进制安全加固特性。 | REA | **先备文件或材料** · ELF、PE 或 Mach-O 文件 | 请用 `rea` 的 `inspect_binary_hardening` 检查我提供的 demo ELF 文件，列出它声明的 PIE、NX 和 RELRO 状态。 | ELF 样例的 PIE 和 RELRO 未启用；NX 缺少声明。 |
| 71 | `inspect_byte_entropy` [〔样例〕](./Codex样例与会话准备.md#item-71) | 计算文件整体或指定区域的字节熵，观察字节分布。 | REA | **先备文件或材料** · 本地二进制文件 | 请用 `rea` 的 `inspect_byte_entropy` 计算我提供的 sample.bin 的整体字节熵，并按 4096 字节分块展示分布。 | 446 字节样例的整体熵为 6.5213 比特/字节。 |

<a name="group-7"></a>

## Windows、Linux 与设备文件（9 项）

| 序号 | 工具名 | 中文用途 | 来源 | 使用条件 | 中文调用示例 | 本次返回 |
|---:|---|---|---|---|---|---|
| 72 | `inspect_pe_imports` [〔样例〕](./Codex样例与会话准备.md#item-72) | 列出 Windows PE 导入的 DLL 及其函数。 | REA | **先备文件或材料** · Windows PE 文件 | 请用 `rea` 的 `inspect_pe_imports` 读取我提供的 demo.exe，按 DLL 分组列出它导入的函数。 | 样例无标准导入或延迟导入，返回 0 个 DLL。 |
| 73 | `inspect_pe_resources` [〔样例〕](./Codex样例与会话准备.md#item-73) | 查看 PE 资源树中的类型、名称、语言和数据范围。 | REA | **先备文件或材料** · 含资源的 PE 文件 | 请用 `rea` 的 `inspect_pe_resources` 查看我提供的 demo.exe 的资源树，列出资源类型和对应的语言编号。 | 找到 3 种资源、5 个条目，含语言编号 1033 和 1041。 |
| 74 | `inspect_pe_certificates` [〔样例〕](./Codex样例与会话准备.md#item-74) | 查看 PE 证书表及其中记录的签名者和算法。 | REA | **先备文件或材料** · 含证书表的 PE 文件 | 请用 `rea` 的 `inspect_pe_certificates` 读取我提供的 demo.exe 的证书表，列出其中记录的签名者和摘要算法。 | 读到 1 个测试签名者和 SHA-256 摘要算法。 |
| 75 | `inspect_windows_shortcut` [〔样例〕](./Codex样例与会话准备.md#item-75) | 读取 Windows 快捷方式记录的路径、参数和工作目录。 | REA | **先备文件或材料** · Windows 快捷方式 | 请用 `rea` 的 `inspect_windows_shortcut` 静态读取我提供的 Demo.lnk，告诉我它记录的目标路径和工作目录。 | 读到相对目标 readme.txt 和工作目录。 |
| 76 | `inspect_ntfs_journal` [〔样例〕](./Codex样例与会话准备.md#item-76) | 检查 NTFS 变更日志记录。 | REA | **先备文件或材料** · 同一 NTFS 卷的 MFT 和 USN 日志 | 请用 `rea` 的 `inspect_ntfs_journal` 使用我提供的同一卷的 MFT 和 USN 日志文件，列出最先读到的十条变更记录。 | 按源顺序读取 3 条变更记录。 |
| 77 | `inspect_elf_notes` [〔样例〕](./Codex样例与会话准备.md#item-77) | 读取 ELF 注记的类型、所有者及数据范围。 | REA | **先备文件或材料** · ELF 文件 | 请用 `rea` 的 `inspect_elf_notes` 读取我提供的 demo ELF 文件，列出注记的所有者和类型，并标出可识别的构建 ID。 | 读取 2 条去重注记，包含 GNU 构建 ID。 |
| 78 | `inspect_kernel_build_config` [〔样例〕](./Codex样例与会话准备.md#item-78) | 从 Linux 内核映像读取构建标识及嵌入的内核配置。 | REA | **先备文件或材料** · 含内嵌内核配置的映像 | 请用 `rea` 的 `inspect_kernel_build_config` 查看我提供的 vmlinux 中嵌入的配置，告诉我 CONFIG_SMP 的记录值。 | 读到 9 项配置，样例未声明 CONFIG_SMP。 |
| 79 | `inspect_kernel_module` [〔样例〕](./Codex样例与会话准备.md#item-79) | 查看 Linux 内核模块的元数据、符号和签名区信息。 | REA | **先备文件或材料** · 未压缩的内核模块 | 请用 `rea` 的 `inspect_kernel_module` 从我提供的 demo.ko 中读取模块名称、许可证以及声明的依赖。 | 模块名 demo，许可证 GPL，依赖字段为空。 |
| 80 | `inspect_devicetree` [〔样例〕](./Codex样例与会话准备.md#item-80) | 解析扁平设备树，查看硬件节点、属性和内存保留区。 | REA | **先备文件或材料** · 设备树 DTB | 请用 `rea` 的 `inspect_devicetree` 读取我提供的 board.dtb，列出根节点下的设备节点及其 compatible 属性。 | 读到根节点下 4 个设备节点；compatible 仅见于根节点。 |

<a name="group-8"></a>

## 编程语言、托管代码与计算模型（15 项）

| 序号 | 工具名 | 中文用途 | 来源 | 使用条件 | 中文调用示例 | 本次返回 |
|---:|---|---|---|---|---|---|
| 81 | `inspect_go_binary` [〔样例〕](./Codex样例与会话准备.md#item-81) | 从 Go 二进制读取编译器、模块、依赖及构建参数。 | REA | **先备文件或材料** · 包含构建信息的 Go 程序 | 请用 `rea` 的 `inspect_go_binary` 检查我提供的 Go 测试程序，列出编译器版本、主模块和依赖模块。 | 读到 go1.26.0、主模块 example.com/tool 和 1 项依赖。 |
| 82 | `inspect_rust_binary` [〔样例〕](./Codex样例与会话准备.md#item-82) | 从含 cargo-auditable 元数据的 Rust 二进制读取依赖。 | REA | **先备文件或材料** · 含 cargo-auditable 元数据的 Rust 程序 | 请用 `rea` 的 `inspect_rust_binary` 从我提供的含 cargo-auditable 元数据的 Rust 测试程序中列出依赖包及版本。 | 读到依赖 itoa，版本 1.0.18。 |
| 83 | `inspect_erlang_beam` [〔样例〕](./Codex样例与会话准备.md#item-83) | 解析 Erlang BEAM 文件中的数据块、原子和导入导出项。 | REA | **先备文件或材料** · Erlang BEAM 文件 | 请用 `rea` 的 `inspect_erlang_beam` 读取我提供的 demo.beam，列出导出函数的名称及参数个数。 | 导出 3 项，包括 start/0、module_info/0 和 module_info/1。 |
| 84 | `inspect_python_pyc` [〔样例〕](./Codex样例与会话准备.md#item-84) | 静态读取 CPython 字节码文件头、代码对象及常量摘要。 | REA | **先备文件或材料** · 支持版本的 CPython 字节码 | 请用 `rea` 的 `inspect_python_pyc` 查看我提供的 demo.pyc，告诉我其对应的 CPython 版本及记录的代码对象名称。 | 识别 CPython 3.12 和两个代码对象。 |
| 85 | `inspect_v8_code_cache` [〔样例〕](./Codex样例与会话准备.md#item-85) | 查看 V8 或 bytenode 代码缓存的文件头和结构。 | REA | **先备文件或材料** · 本地 V8 缓存文件 | 请用 `rea` 的 `inspect_v8_code_cache` 读取我提供的 demo.jsc，列出可识别的 V8 缓存文件头字段。 | 识别 32 字节缓存头并返回字段。 |
| 86 | `inspect_managed_artifact` [〔样例〕](./Codex样例与会话准备.md#item-86) | 查看 .NET 托管程序集的标识与 PE/CLI 元数据。 | REA | **先备文件或材料** · .NET 托管程序集 | 请用 `rea` 的 `inspect_managed_artifact` 读取我提供的 Demo.dll，告诉我程序集名称、版本和托管元数据概况。 | 程序集为 Fixture.Managed，版本 1.2.3.4。 |
| 87 | `compare_managed_members` [〔准备〕](./Codex样例与会话准备.md#item-87) | 对比两组已有的托管成员记录，识别对应成员及差异。 | REA | **先备会话或前序结果** · 新旧两份托管成员证据 | 请用 `rea` 的 `compare_managed_members` 比较我提供的新旧两份 REA 托管成员证据，列出能够匹配的成员及其签名变化。 | 精确匹配 2 个成员，样例签名未变。 |
| 88 | `inspect_managed_native_boundaries` [〔样例〕](./Codex样例与会话准备.md#item-88) | 查看 .NET 程序集中的 P/Invoke 等原生调用声明。 | REA | **先备文件或材料** · 含 P/Invoke 声明的 .NET 程序集 | 请用 `rea` 的 `inspect_managed_native_boundaries` 从我提供的 Demo.dll 列出 P/Invoke 声明及各自引用的原生库。 | Main 从 libdemo.dylib 导入 demo_value。 |
| 89 | `verify_managed_native_boundaries` [〔准备〕](./Codex样例与会话准备.md#item-89) | 将托管调用声明与已有的原生导出或函数记录核对。 | REA | **先备会话或前序结果** · P/Invoke 证据及匹配动态库的 Mach-O 导出证据 | 请用 `rea` 的 `verify_managed_native_boundaries` 用本对话的 P/Invoke 声明证据和对应动态库的 inspect_macho 导出证据，逐项核对入口名并说明匹配依据。 | 确认 demo_value 与 _demo_value 精确匹配。 |
| 90 | `project_managed_application_graph` [〔准备〕](./Codex样例与会话准备.md#item-90) | 将托管程序集、成员及原生调用关系整理为应用关系图。 | REA | **先备会话或前序结果** · REA 托管成员证据 | 请用 `rea` 的 `project_managed_application_graph` 使用我提供的 REA 托管成员证据生成 .NET 应用关系图，列出其中可识别的类型与成员。 | 生成 5 个节点和 5 条边，识别类型、方法及字段。 |
| 91 | `inspect_il2cpp_metadata` [〔样例〕](./Codex样例与会话准备.md#item-91) | 查看 Unity IL2CPP 元数据表及可关联的原生方法。 | REA | **先备文件或材料** · IL2CPP 元数据文件 | 请用 `rea` 的 `inspect_il2cpp_metadata` 读取我提供的 Unity 测试项目的 global-metadata.dat，列出元数据版本和可识别的表。 | 版本 39，识别 31 个表或数据区段。 |
| 92 | `inspect_wasm_artifact` [〔样例〕](./Codex样例与会话准备.md#item-92) | 使用 WABT 验证 WebAssembly 模块并查看段、导入导出和 WAT 表示。 | REA | **先备文件或材料** · WebAssembly 模块 | 请用 `rea` 的 `inspect_wasm_artifact` 验证我提供的 demo.wasm，列出模块导入和导出的名称。 | 通过验证，导出 hello，导入 0 项。 |
| 93 | `compare_wasm_interfaces` [〔准备〕](./Codex样例与会话准备.md#item-93) | 对比两个 WebAssembly 模块导入导出项的名称、种类和签名。 | REA | **先备会话或前序结果** · 两份 WASM 检查证据 | 请用 `rea` 的 `compare_wasm_interfaces` 比较本对话中两份 WASM 模块检查结果，列出新增、移除或签名变化的导出项。 | 新版新增 greet，移除 hello。 |
| 94 | `inspect_gpu_code_objects` [〔样例〕](./Codex样例与会话准备.md#item-94) | 查看 CUDA 或 HIP 代码对象及内核条目。 | REA | **先备文件或材料** · CUDA 或 HIP 代码对象 | 请用 `rea` 的 `inspect_gpu_code_objects` 盘点我提供的 demo.cubin，列出可识别的 GPU 目标架构。 | 从 CUBIN 识别到 sm_80 架构。 |
| 95 | `inspect_model_artifact` [〔样例〕](./Codex样例与会话准备.md#item-95) | 读取 GGUF 或 safetensors 模型的元数据和张量声明。 | REA | **先备文件或材料** · GGUF 或 safetensors 模型文件 | 请用 `rea` 的 `inspect_model_artifact` 读取我提供的 demo.safetensors，列出每个张量的名称、数据类型和形状。 | 读取张量 example，类型 F32，形状 [1]。 |

<a name="group-9"></a>

## 文件、应用包与数据库（5 项）

| 序号 | 工具名 | 中文用途 | 来源 | 使用条件 | 中文调用示例 | 本次返回 |
|---:|---|---|---|---|---|---|
| 96 | `inspect_artifact` [〔准备〕](./Codex样例与会话准备.md#item-96) | 识别本地文件或应用包，查看支持格式的内容清单。 | REA | **先备会话或前序结果** · 已打开的归档 | 请用 `rea` 的 `inspect_artifact` 检查当前已打开的 demo.zip，列出内部文件的路径和条目标识。 | 列出 README.txt 及其条目标识。 |
| 97 | `extract_artifact` [〔准备〕](./Codex样例与会话准备.md#item-97) | 从已打开的归档中将全部或选定文件解包到本地目录。 | REA | **先备会话或前序结果** · 已打开的归档、条目标识及新输出目录 | 请用 `rea` 的 `extract_artifact` 按上一条清单中 README.txt 的条目标识，只把这个文件解包到工作区新目录 demo-extract。 | 按条目标识实际解包 README.txt，共 36 字节。 |
| 98 | `inspect_desktop_application` [〔样例〕](./Codex样例与会话准备.md#item-98) | 从桌面应用目录识别可能使用的框架和运行时。 | REA | **先备文件或材料** · 桌面应用安装目录 | 请用 `rea` 的 `inspect_desktop_application` 检查我提供的桌面应用安装目录，根据文件和元数据列出可能使用的运行时。 | 检查了 6 个目录条目，样例未命中已知运行时标记。 |
| 99 | `audit_release_exposure` [〔样例〕](./Codex样例与会话准备.md#item-99) | 检查已发布应用包中仍可被静态读取的信息。 | REA | **先备文件或材料** · 待检查的发布包 | 请用 `rea` 的 `audit_release_exposure` 检查我自己的 Demo.app 发布包，列出可从成品静态读取的信息及对应文件。 | 在已评估项目中没有命中暴露项；部分检查依赖产物格式。 |
| 100 | `inspect_sqlite_database` [〔样例〕](./Codex样例与会话准备.md#item-100) | 读取 SQLite 快照的表结构，可查看指定列和记录。 | REA | **先备文件或材料** · SQLite 快照及存在的表、列 | 请用 `rea` 的 `inspect_sqlite_database` 从我提供的 demo.sqlite 快照的 products 表中读取前五行，只显示 id 和 name 两列。 | 从 products 读到 id 为 1、名称为“纸杯”的记录。 |

<a name="group-10"></a>

## 证据、版本差异与重建验证（17 项）

本机实测中，证据包的导入、导出和对比使用临时会话的空包；进程对比和静态与运行时关联使用离线合成记录；环境包导出使用手写 HAR。

| 序号 | 工具名 | 中文用途 | 来源 | 使用条件 | 中文调用示例 | 本次返回 |
|---:|---|---|---|---|---|---|
| 101 | `get_evidence_bundle` | 读取当前会话保留的分析证据及待解问题。 | REA | **直接用** · 查询当前会话的证据摘要 | 请用 `rea` 的 `get_evidence_bundle` 以摘要列出当前会话保留的证据，给出记录 ID 和产生记录的工具。 | 新对话返回 0 条；有调查记录的对话返回 2 条。 |
| 102 | `export_evidence_bundle` | 把当前会话的证据包写入本地文件。 | REA | **直接用** · 可写工作区及未占用的输出文件名 | 请用 `rea` 的 `export_evidence_bundle` 把本次测试会话的证据包保存为工作区中新文件 demo-evidence.json。 | 全新会话也能导出，得到 105 字节空证据包。 |
| 103 | `import_evidence_bundle` [〔样例〕](./Codex样例与会话准备.md#item-103) | 校验证据包后，将其中的记录合并到当前会话。 | REA | **先备文件或材料** · REA 证据包 JSON | 请用 `rea` 的 `import_evidence_bundle` 校验我提供的 demo-evidence.json，并把通过校验的记录导入当前测试会话。 | 校验并导入空包，新增 0 条记录。 |
| 104 | `compare_bundles` [〔样例〕](./Codex样例与会话准备.md#item-104) | 比较两份分析证据包。 | REA | **先备文件或材料** · 两个 REA 证据包文件 | 请用 `rea` 的 `compare_bundles` 对比我提供的 before-evidence.json 和 after-evidence.json，概括证据记录的差异。 | 两个相同的空包返回 unchanged。 |
| 105 | `compare_artifacts` [〔准备〕](./Codex样例与会话准备.md#item-105) | 比较两份分析产物记录中的差异。 | REA | **先备会话或前序结果** · 两份完整的产物清单证据 | 请用 `rea` 的 `compare_artifacts` 比较本对话中旧版和新版安装包的两份文件清单证据，列出新增和内容变化的文件。 | 发现根产物内容变化，未报告新增文件。 |
| 106 | `compare_process_captures` [〔准备〕](./Codex样例与会话准备.md#item-106) | 对比两份已有的进程观测记录。 | REA | **先备会话或前序结果** · 两份兼容的进程记录 | 请用 `rea` 的 `compare_process_captures` 对比我提供的同一测试命令前后两次的 REA 进程记录，告诉我终端输出有什么变化。 | 离线合成记录的终端输出一致。 |
| 107 | `find_changed_behavior` [〔准备〕](./Codex样例与会话准备.md#item-107) | 汇总已有的进程、产物和函数比较结果，定位行为变化。 | REA | **先备会话或前序结果** · 前序产物或进程比较证据 | 请用 `rea` 的 `find_changed_behavior` 汇总本对话中已有的产物和进程比较证据，指出哪些行为有可核实的变化。 | 识别到静态产物差异，未确认运行行为变化。 |
| 108 | `correlate_static_and_runtime` [〔准备〕](./Codex样例与会话准备.md#item-108) | 用已有的静态和运行时比较结果核对指定的关联假设。 | REA | **先备会话或前序结果** · 静态与运行时比较证据及配对假设 | 请用 `rea` 的 `correlate_static_and_runtime` 使用本对话的函数比较和进程比较证据，按旧版对应旧版、新版对应新版，核对该函数的变化是否伴随终端输出变化。 | 函数文本变化，终端输出一致；版本对应关系未经独立验证。 |
| 109 | `build_reconstruction_obligation_ledger` [〔样例〕](./Codex样例与会话准备.md#item-109) | 整理重建工作需要验证的事项及相应证据。 | REA | **先备文件或材料** · 证据包、已审阅事项及重建清单 | 请用 `rea` 的 `build_reconstruction_obligation_ledger` 根据我提供的 REA 证据包、已审阅事项和重建清单，列出仍需验证的事项。 | 空清单返回 0 项待验证事项，覆盖状态为 partial。 |
| 110 | `evaluate_reconstruction_coverage` [〔样例〕](./Codex样例与会话准备.md#item-110) | 检查指定范围的重建验证覆盖了哪些要求、还缺哪些证据。 | REA | **先备文件或材料** · 覆盖评估数据及边界 ID | 请用 `rea` 的 `evaluate_reconstruction_coverage` 使用我提供的覆盖评估输入，检查 replacement.cli 这个边界还有哪些要求缺少验证证据。 | replacement.cli 返回部分覆盖，列出 4 个缺口。 |
| 111 | `verify_reconstruction` [〔准备〕](./Codex样例与会话准备.md#item-111) | 按明确列出的行为和结构要求核验重建结果。 | REA | **先备会话或前序结果** · 验证规格及其引用的比较证据 | 请用 `rea` 的 `verify_reconstruction` 按我提供的重建规格和本会话的证据，核验两版测试命令的终端输出是否满足规格中的一致性要求。 | 唯一声明的终端输出一致性要求通过。 |
| 112 | `record_unknown` | 将尚未解决的问题记入调查记录。 | REA | **直接用** · 提供问题及结案标准即可 | 请用 `rea` 的 `record_unknown` 在“离线输出”领域登记中等严重度问题“相同输入是否生成相同摘要”，以受控重放的实测结果为结案依据，暂不指定环境、关联记录或后续探针，并返回问题 ID。 | 创建 1 个中等严重度待解问题，返回问题 ID。 |
| 113 | `list_unknowns` | 按状态、严重程度或领域列出待解问题。 | REA | **直接用** · 可直接查询，列表允许为空 | 请用 `rea` 的 `list_unknowns` 列出当前调查中严重度为中等的待解问题，最多显示十条。 | 新对话返回 0 条；登记问题后返回 1 条。 |
| 114 | `update_unknown` [〔准备〕](./Codex样例与会话准备.md#item-114) | 更新已记录问题的内容或处理状态。 | REA | **先备会话或前序结果** · 已有问题 ID 及当前修订号 | 请用 `rea` 的 `update_unknown` 使用上一条问题的 ID 和当前修订号，将该问题的处理状态更新为调查中。 | 状态变为调查中，修订号从 1 升至 2。 |
| 115 | `verify_unknown_resolution` [〔准备〕](./Codex样例与会话准备.md#item-115) | 对照证据核验某个问题是否满足结案条件。 | REA | **先备会话或前序结果** · 已有问题 ID 及当前证据 | 请用 `rea` 的 `verify_unknown_resolution` 根据我选中的问题 ID 和当前证据，说明它是否满足结案条件。 | 报告缺少受控重放证据，问题尚不满足结案条件。 |
| 116 | `export_environment_bundle` [〔准备〕](./Codex样例与会话准备.md#item-116) | 将已保存的浏览器场景或 HAR 证据导出为本地环境包。 | REA | **先备会话或前序结果** · 已分析的 HAR 证据及新的输出目录 | 请用 `rea` 的 `export_environment_bundle` 用本对话中合成 HAR 的分析证据，把测试环境包导出到工作区新目录 demo-environment。 | 由 1 条合成 HAR 记录实际生成环境包，共 7 个文件。 |
| 117 | `reset_investigation` [〔准备〕](./Codex样例与会话准备.md#item-117) | 清空当前调查保留的证据和问题历史。 | REA | **先备会话或前序结果** · 专用测试调查及新的备份文件名 | 请用 `rea` 的 `reset_investigation` 将当前临时测试调查的证据保存到工作区新文件 before-reset.json，再清空这次调查的证据和问题历史。 | 导出含 1 条记录的备份，再清空本轮测试调查。 |

<a name="group-11"></a>

## 工作指南、设置与结果浏览（6 项）

| 序号 | 工具名 | 中文用途 | 来源 | 使用条件 | 中文调用示例 | 本次返回 |
|---:|---|---|---|---|---|---|
| 118 | `guided_workflows` | 浏览 REA 自带的工作流程及操作指南。 | REA | **直接用** · 本机已安装 REA 指南 | 请用 `rea` 的 `guided_workflows` 列出 REA 内置的工作流程，并指出哪一个适合初次检查应用包。 | 列出 6 个内置工作流程。 |
| 119 | `search_guidance` | 按关键词查找已安装的 REA 指南章节。 | REA | **直接用** · 本机已安装 REA 指南 | 请用 `rea` 的 `search_guidance` 在已安装的指南中搜索 JavaScript module，给出最相关的三个章节及定位信息。 | 关键词命中 10 章，给出前三章及定位信息。 |
| 120 | `read_guidance_section` [〔准备〕](./Codex样例与会话准备.md#item-120) | 读取选定的指南章节。 | REA | **先备会话或前序结果** · 上次指南搜索返回的章节定位符 | 请用 `rea` 的 `read_guidance_section` 用上一条指南搜索结果中第一项的定位信息读取该节，并概括操作步骤。 | 成功读到首个匹配章节及操作步骤。 |
| 121 | `inspect_analysis_settings` | 查看分析的大小限制、超时和工作进程内存设置。 | REA | **直接用** · 指定设置名即可 | 请用 `rea` 的 `inspect_analysis_settings` 查看 asar.max_header_bytes 的当前值、允许范围和生效时机。 | 读到 ASAR 文件头限制默认值 16 MiB 及允许范围。 |
| 122 | `update_analysis_settings` | 调整或重置后续分析任务使用的运行时设置。 | REA | **直接用** · 指定设置及重置动作即可 | 请用 `rea` 的 `update_analysis_settings`，按参数 {"changes":[{"setting":"asar.max_header_bytes","action":"reset"}]} 仅将本次 REA 服务的这一项恢复到启动值，报告恢复后的值和 changed 标志。 | 恢复到启动值；原值已经相同，返回 changed=false。 |
| 123 | `inspect_analysis_view` [〔准备〕](./Codex样例与会话准备.md#item-123) | 按视图读取已保留的分析结果，支持分段浏览。 | REA | **先备会话或前序结果** · 接口对比摘要的父证据 ID 及对应视图 | 请用 `rea` 的 `inspect_analysis_view` 使用刚得到的接口对比摘要中的 parent_evidence_id，在 endpoint-comparison 视图的 static-endpoints 集合中读取前十条接口记录。 | 从 static-endpoints 读到 /demo/report，与 HAR 匹配。 |
