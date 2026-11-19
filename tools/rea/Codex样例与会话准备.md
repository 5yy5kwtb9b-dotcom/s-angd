# REA 中文示例的测试样例与会话准备

从原清单点序号旁的“样例”或“准备”可直达对应段落。每个文本框都可以整段复制到已打开本仓库的 Codex 对话。单独下载时，把 ZIP 和所选指令一起交给 Codex。

同一组步骤使用同一 REA 会话。可复用已经解压的目录。抓包、归档、安装包和二进制均作本地样例读取；Android 示例只需 APK 文件。浏览器、Node 和 Electron 的会话使用专用进程，回环端口和目标 ID 由启动器当场返回，十分钟后自动退出。

文件包内含 Android 样例源码、两版 JavaScript、配对证据参数和上游 MIT 许可。第 44 项另从本机系统应用取 Assets.car，第 14 项使用本机或临时下载的 Electron 运行时。原清单的“本次返回”保留上一轮对话记录；更换样例后应以当前返回为准。

[下载可复用样例包](./测试样例.zip) · [返回 123 项中文清单](./Codex对话可用工具中文清单.md)

## 这份样例包的复核结果

在这台 Apple 芯片 Mac 上，通过 Codex 的 MCP 连接逐项调用，50 条文件类、58 条会话类均收到有效返回。文件类从最终 ZIP 解压到含空格和中文的目录后复测。会话类使用样例产生的证据、地址或目标 ID。此轮核验了样例和工具参数，上一轮逐句发送中文的记录保存在[对话实测 JSON](./Codex中文示例逐条实测.json)。

| 编号 | 可用来核对的返回 |
|---|---|
| 2、3 | 两帧分别为 60 和 74 字节，线上合计 134 字节，间隔 1 秒。 |
| 14 | Electron 45.4.1 主框架的 file_path 指向样例中的 live/page.html。 |
| 20、24 | source map 指向 main.ts；新版 getProfile 的返回属性多了 count。 |
| 29–32、34 | Android 包名 demo.fixture，目标 SDK 28；v1 签名含一个证书指纹。可读到 MainActivity、默认字符串 Fixture cup 和中文“样例纸杯”。 |
| 89、93 | 托管声明与 libdemo.dylib 的入口可核对；新版 WASM 新增 greet，移除 hello。 |
| 100、103 | products 首行是 1、纸杯；members.json 中有两条可导入的托管成员记录。 |
| 110、117 | replacement.cli 报告部分覆盖；在新的调查中保存了一条 HAR 证据，备份后清空成功。 |

## 50 条文件类示例

[查看 50 条原文的首轮与修订复测结果](./50条文件示例全新对话实测.md)

### 抓包与网络记录

<a id="item-2"></a>

#### 2 · `inspect_packet_capture`（Mac 替代）

样例文件　`web/两帧样例.pcap`

```text
定位本仓库 tools/rea/测试样例.zip，在临时目录解压，以下路径均相对于包内 samples/。
本项输入按顺序为 web/两帧样例.pcap。
请用 mac_pcap 的 inspect_packet_capture 读取我提供的 web/两帧样例.pcap，按帧号列出 frame.number 和 frame.len。
```

<a id="item-3"></a>

#### 3 · `inspect_pcap_capture`（Mac 替代）

样例文件　`web/两帧样例.pcap`

```text
定位本仓库 tools/rea/测试样例.zip，在临时目录解压，以下路径均相对于包内 samples/。
本项输入按顺序为 web/两帧样例.pcap。
请用 mac_pcap 的 inspect_pcap_capture 汇总我提供的 web/两帧样例.pcap，告诉我包数、线上字节总数和持续时间。
```

<a id="item-5"></a>

#### 5 · `inspect_web_network_capture`

样例文件　`web/requests.har`

```text
定位本仓库 tools/rea/测试样例.zip，在临时目录解压，以下路径均相对于包内 samples/。
本项输入按顺序为 web/requests.har。
请用 rea 的 inspect_web_network_capture 读取我提供的 web/requests.har，按记录顺序列出前五个请求的方法、路径和响应状态码。
```

### 网页、浏览器与 Electron

<a id="item-13"></a>

#### 13 · `inspect_playwright_trace`

样例文件　`web/trace.zip`

```text
定位本仓库 tools/rea/测试样例.zip，在临时目录解压，以下路径均相对于包内 samples/。
本项输入按顺序为 web/trace.zip。
请用 rea 的 inspect_playwright_trace 读取我提供的 web/trace.zip，按记录顺序列出前十条网络事件。
```

<a id="item-15"></a>

#### 15 · `inspect_electron_fuses`

样例文件　`electron/Demo.app`

```text
定位本仓库 tools/rea/测试样例.zip，在临时目录解压，以下路径均相对于包内 samples/。
本项输入按顺序为 electron/Demo.app。
请用 rea 的 inspect_electron_fuses 检查我提供的 electron/Demo.app，列出其中 Electron 功能开关的名称和当前值。
```

### JavaScript、源码映射与 API

<a id="item-16"></a>

#### 16 · `analyze_javascript_application`

样例文件　`js/app.asar`

```text
定位本仓库 tools/rea/测试样例.zip，在临时目录解压，以下路径均相对于包内 samples/。
本项输入按顺序为 js/app.asar。
请用 rea 的 analyze_javascript_application 分析我提供的 js/app.asar，列出入口模块及其直接导入的模块。
```

<a id="item-19"></a>

#### 19 · `trace_web_module_imports`

样例文件　`web/exported-traces/manifest.json`

```text
定位本仓库 tools/rea/测试样例.zip，在临时目录解压，以下路径均相对于包内 samples/。
本项输入按顺序为 web/exported-traces/manifest.json。
请用 rea 的 trace_web_module_imports 读取我提供的脚本导出清单 web/exported-traces/manifest.json，列出编号 0 的脚本导入了哪些模块。
```

<a id="item-20"></a>

#### 20 · `trace_web_source_location`

样例文件　`web/exported-traces/manifest.json`、`web/main.js.map`

```text
定位本仓库 tools/rea/测试样例.zip，在临时目录解压，以下路径均相对于包内 samples/。
先用 unzip 将整个测试样例.zip 完整解压到新临时目录，保留 samples/web/exported-traces/files/ 及其所有子目录。确认编号 0 对应的 main.js、web/exported-traces/manifest.json 和 web/main.js.map 三者都在，再调用工具。使用下面的工具参数，把两个占位符换成本次解压后的绝对路径。
{"manifest_path":"<manifest.json绝对路径>","script_index":0,"generated_position":{"line":1,"column":0},"source_map":{"path":"<main.js.map绝对路径>","url":"https://example.test/main.js.map"}}
请用 rea 的 trace_web_source_location 用我提供的脚本清单、配套 source map 本地路径和原始 URL，将编号 0 的脚本第 1 行、第 0 列映射回源码。
```

<a id="item-21"></a>

#### 21 · `export_web_scripts`

样例文件　`web/web-scenario1.json`

```text
定位本仓库 tools/rea/测试样例.zip，在临时目录解压，以下路径均相对于包内 samples/。
本项输入按顺序为 web/web-scenario1.json。输出写入新建临时工作目录下尚不存在的 scripts-export。
请用 rea 的 export_web_scripts 从我提供的页面检查记录 web/web-scenario1.json 导出已保存的脚本，将脚本和清单写入工作区新目录 scripts-export。
```

<a id="item-28"></a>

#### 28 · `inspect_api_contract`

样例文件　`web/openapi.json`

```text
定位本仓库 tools/rea/测试样例.zip，在临时目录解压，以下路径均相对于包内 samples/。
本项输入按顺序为 web/openapi.json。
请用 rea 的 inspect_api_contract 读取我提供的 web/openapi.json，按路径列出声明的 HTTP 方法。
```

### Android、ADB、Flutter 与鸿蒙

<a id="item-29"></a>

#### 29 · `inspect_android_package`

样例文件　`mobile/Demo.apk`

```text
定位本仓库 tools/rea/测试样例.zip，在临时目录解压，以下路径均相对于包内 samples/。
本项输入按顺序为 mobile/Demo.apk。
请用 rea 的 inspect_android_package 查看我提供的 mobile/Demo.apk，列出包名、目标 SDK 和声明的权限。
```

<a id="item-30"></a>

#### 30 · `inspect_apk_signature`

样例文件　`mobile/Demo.apk`

```text
定位本仓库 tools/rea/测试样例.zip，在临时目录解压，以下路径均相对于包内 samples/。
本项输入按顺序为 mobile/Demo.apk。
请用 rea 的 inspect_apk_signature 读取我提供的 mobile/Demo.apk，列出检测到的签名方案和签名证书指纹。
```

<a id="item-31"></a>

#### 31 · `search_android_classes`

样例文件　`mobile/Demo.apk`

```text
定位本仓库 tools/rea/测试样例.zip，在临时目录解压，以下路径均相对于包内 samples/。
本项输入按顺序为 mobile/Demo.apk。
请用 rea 的 search_android_classes 在我提供的 mobile/Demo.apk 中搜索名称含 Activity 的类，列出完整类名。
```

<a id="item-32"></a>

#### 32 · `inspect_android_class`

样例文件　`mobile/Demo.apk`

```text
定位本仓库 tools/rea/测试样例.zip，在临时目录解压，以下路径均相对于包内 samples/。
本项输入按顺序为 mobile/Demo.apk。选用样例内的完整类名 demo.fixture.MainActivity。
请用 rea 的 inspect_android_class 在我提供的 APK 里，读取demo.fixture.MainActivity，列出该类声明的字段和方法。
```

<a id="item-34"></a>

#### 34 · `decode_android_resources`

样例文件　`mobile/Demo.apk`

```text
定位本仓库 tools/rea/测试样例.zip，在临时目录解压，以下路径均相对于包内 samples/。
本项输入按顺序为 mobile/Demo.apk。先读取默认表，再指定 locales 为 ["zh"] 读中文表；每个表各举一个字符串。
请用 rea 的 decode_android_resources 解码我提供的 mobile/Demo.apk，列出实际包含的语言资源，并从每种语言中举一个字符串示例。
```

<a id="item-38"></a>

#### 38 · `identify_flutter_build`

样例文件　`mobile/flutter.apk`

```text
定位本仓库 tools/rea/测试样例.zip，在临时目录解压，以下路径均相对于包内 samples/。
本项输入按顺序为 mobile/flutter.apk。
请用 rea 的 identify_flutter_build 检查我提供的 Flutter 安装包 mobile/flutter.apk，列出其中的 ABI 和可识别的 Dart 快照标识。
```

<a id="item-39"></a>

#### 39 · `inspect_dart_aot`

样例文件　`mobile/flutter.apk`

```text
定位本仓库 tools/rea/测试样例.zip，在临时目录解压，以下路径均相对于包内 samples/。
本项输入按顺序为 mobile/flutter.apk。
请用 rea 的 inspect_dart_aot 读取我提供的旧版 Flutter 测试 APK 中 arm64-v8a 的 Dart AOT 快照，概括可识别的结构。
```

### Apple 应用、Swift 与 Objective-C

<a id="item-42"></a>

#### 42 · `open_bundle_resources`

样例文件　`apple/Demo.app`

```text
定位本仓库 tools/rea/测试样例.zip，在临时目录解压，以下路径均相对于包内 samples/。
本项输入按顺序为 apple/Demo.app。
请用 rea 的 open_bundle_resources 以只读方式打开我提供的 apple/Demo.app 资源目录，告诉我当前选中了哪个应用包。
```

<a id="item-49"></a>

#### 49 · `inspect_apple_ips`

样例文件　`apple/Demo.ips`

```text
定位本仓库 tools/rea/测试样例.zip，在临时目录解压，以下路径均相对于包内 samples/。
本项输入按顺序为 apple/Demo.ips。
请用 rea 的 inspect_apple_ips 读取我提供的 apple/Demo.ips 崩溃报告，找出异常类型和触发崩溃的线程。
```

### 原生二进制、符号与分析会话

<a id="item-54"></a>

#### 54 · `open_binary`

样例文件　`native/demo`

```text
定位本仓库 tools/rea/测试样例.zip，在临时目录解压，以下路径均相对于包内 samples/。
本项输入按顺序为 native/demo。
请用 rea 的 open_binary 用 Ghidra 打开我提供的 native/demo，并报告识别到的文件格式。
```

<a id="item-69"></a>

#### 69 · `inspect_native_exports`

样例文件　`native/libdemo.so`

```text
定位本仓库 tools/rea/测试样例.zip，在临时目录解压，以下路径均相对于包内 samples/。
本项输入按顺序为 native/libdemo.so。
请用 rea 的 inspect_native_exports 从我提供的 native/libdemo.so 列出已定义的动态导出符号，先显示前十个。
```

<a id="item-70"></a>

#### 70 · `inspect_binary_hardening`

样例文件　`native/go.elf`

```text
定位本仓库 tools/rea/测试样例.zip，在临时目录解压，以下路径均相对于包内 samples/。
本项输入按顺序为 native/go.elf。
请用 rea 的 inspect_binary_hardening 检查我提供的 native/go.elf，列出它声明的 PIE、NX 和 RELRO 状态。
```

<a id="item-71"></a>

#### 71 · `inspect_byte_entropy`

样例文件　`native/kernel.bin`

```text
定位本仓库 tools/rea/测试样例.zip，在临时目录解压，以下路径均相对于包内 samples/。
本项输入按顺序为 native/kernel.bin。
请用 rea 的 inspect_byte_entropy 计算我提供的 native/kernel.bin 的整体字节熵，并按 4096 字节分块展示分布。
```

### Windows、Linux 与设备文件

<a id="item-72"></a>

#### 72 · `inspect_pe_imports`

样例文件　`native/native.exe`

```text
定位本仓库 tools/rea/测试样例.zip，在临时目录解压，以下路径均相对于包内 samples/。
本项输入按顺序为 native/native.exe。
请用 rea 的 inspect_pe_imports 读取我提供的 native/native.exe，按 DLL 分组列出它导入的函数。
```

<a id="item-73"></a>

#### 73 · `inspect_pe_resources`

样例文件　`native/resources.exe`

```text
定位本仓库 tools/rea/测试样例.zip，在临时目录解压，以下路径均相对于包内 samples/。
本项输入按顺序为 native/resources.exe。
请用 rea 的 inspect_pe_resources 查看我提供的 native/resources.exe 的资源树，列出资源类型和对应的语言编号。
```

<a id="item-74"></a>

#### 74 · `inspect_pe_certificates`

样例文件　`native/certificate.exe`

```text
定位本仓库 tools/rea/测试样例.zip，在临时目录解压，以下路径均相对于包内 samples/。
本项输入按顺序为 native/certificate.exe。
请用 rea 的 inspect_pe_certificates 读取我提供的 native/certificate.exe 的证书表，列出其中记录的签名者和摘要算法。
```

<a id="item-75"></a>

#### 75 · `inspect_windows_shortcut`

样例文件　`native/readme.lnk`

```text
定位本仓库 tools/rea/测试样例.zip，在临时目录解压，以下路径均相对于包内 samples/。
本项输入按顺序为 native/readme.lnk。
请用 rea 的 inspect_windows_shortcut 静态读取我提供的 native/readme.lnk，告诉我它记录的目标路径和工作目录。
```

<a id="item-76"></a>

#### 76 · `inspect_ntfs_journal`

样例文件　`native/records`、`native/journal`

```text
定位本仓库 tools/rea/测试样例.zip，在临时目录解压，以下路径均相对于包内 samples/。
本项输入按顺序为 native/records 和 native/journal。records 是 MFT，journal 是同一合成卷的 USN。
请用 rea 的 inspect_ntfs_journal 使用我提供的同一卷的 MFT 和 USN 日志文件，列出最先读到的十条变更记录。
```

<a id="item-77"></a>

#### 77 · `inspect_elf_notes`

样例文件　`native/notes.elf`

```text
定位本仓库 tools/rea/测试样例.zip，在临时目录解压，以下路径均相对于包内 samples/。
本项输入按顺序为 native/notes.elf。
请用 rea 的 inspect_elf_notes 读取我提供的 native/notes.elf，列出注记的所有者和类型，并标出可识别的构建 ID。
```

<a id="item-78"></a>

#### 78 · `inspect_kernel_build_config`

样例文件　`native/kernel.bin`

```text
定位本仓库 tools/rea/测试样例.zip，在临时目录解压，以下路径均相对于包内 samples/。
本项输入按顺序为 native/kernel.bin。
请用 rea 的 inspect_kernel_build_config 查看我提供的 native/kernel.bin 中嵌入的配置，告诉我 CONFIG_SMP 的记录值。
```

<a id="item-79"></a>

#### 79 · `inspect_kernel_module`

样例文件　`native/module.ko`

```text
定位本仓库 tools/rea/测试样例.zip，在临时目录解压，以下路径均相对于包内 samples/。
本项输入按顺序为 native/module.ko。
请用 rea 的 inspect_kernel_module 从我提供的 native/module.ko 中读取模块名称、许可证以及声明的依赖。
```

<a id="item-80"></a>

#### 80 · `inspect_devicetree`

样例文件　`native/device.dtb`

```text
定位本仓库 tools/rea/测试样例.zip，在临时目录解压，以下路径均相对于包内 samples/。
本项输入按顺序为 native/device.dtb。
请用 rea 的 inspect_devicetree 读取我提供的 native/device.dtb，列出根节点下的设备节点及其 compatible 属性。
```

### 编程语言、托管代码与计算模型

<a id="item-81"></a>

#### 81 · `inspect_go_binary`

样例文件　`native/go.elf`

```text
定位本仓库 tools/rea/测试样例.zip，在临时目录解压，以下路径均相对于包内 samples/。
本项输入按顺序为 native/go.elf。
请用 rea 的 inspect_go_binary 检查我提供的 Go 测试程序，列出编译器版本、主模块和依赖模块。
```

<a id="item-82"></a>

#### 82 · `inspect_rust_binary`

样例文件　`native/rust.elf`

```text
定位本仓库 tools/rea/测试样例.zip，在临时目录解压，以下路径均相对于包内 samples/。
本项输入按顺序为 native/rust.elf。
请用 rea 的 inspect_rust_binary 从我提供的含 cargo-auditable 元数据的 Rust 测试程序中列出依赖包及版本。
```

<a id="item-83"></a>

#### 83 · `inspect_erlang_beam`

样例文件　`native/sample.beam`

```text
定位本仓库 tools/rea/测试样例.zip，在临时目录解压，以下路径均相对于包内 samples/。
本项输入按顺序为 native/sample.beam。
请用 rea 的 inspect_erlang_beam 读取我提供的 native/sample.beam，列出导出函数的名称及参数个数。
```

<a id="item-84"></a>

#### 84 · `inspect_python_pyc`

样例文件　`native/sample.pyc`

```text
定位本仓库 tools/rea/测试样例.zip，在临时目录解压，以下路径均相对于包内 samples/。
本项输入按顺序为 native/sample.pyc。
请用 rea 的 inspect_python_pyc 查看我提供的 native/sample.pyc，告诉我其对应的 CPython 版本及记录的代码对象名称。
```

<a id="item-85"></a>

#### 85 · `inspect_v8_code_cache`

样例文件　`native/sample.jsc`

```text
定位本仓库 tools/rea/测试样例.zip，在临时目录解压，以下路径均相对于包内 samples/。
本项输入按顺序为 native/sample.jsc。
请用 rea 的 inspect_v8_code_cache 读取我提供的 native/sample.jsc，列出可识别的 V8 缓存文件头字段。
```

<a id="item-86"></a>

#### 86 · `inspect_managed_artifact`

样例文件　`native/Interop.dll`

```text
定位本仓库 tools/rea/测试样例.zip，在临时目录解压，以下路径均相对于包内 samples/。
本项输入按顺序为 native/Interop.dll。
请用 rea 的 inspect_managed_artifact 读取我提供的 native/Interop.dll，告诉我程序集名称、版本和托管元数据概况。
```

<a id="item-88"></a>

#### 88 · `inspect_managed_native_boundaries`

样例文件　`native/Interop.dll`

```text
定位本仓库 tools/rea/测试样例.zip，在临时目录解压，以下路径均相对于包内 samples/。
本项输入按顺序为 native/Interop.dll。
请用 rea 的 inspect_managed_native_boundaries 从我提供的 native/Interop.dll 列出 P/Invoke 声明及各自引用的原生库。
```

<a id="item-91"></a>

#### 91 · `inspect_il2cpp_metadata`

样例文件　`native/global-metadata.dat`

```text
定位本仓库 tools/rea/测试样例.zip，在临时目录解压，以下路径均相对于包内 samples/。
本项输入按顺序为 native/global-metadata.dat。
请用 rea 的 inspect_il2cpp_metadata 读取我提供的 Unity 测试项目的 native/global-metadata.dat，列出元数据版本和可识别的表。
```

<a id="item-92"></a>

#### 92 · `inspect_wasm_artifact`

样例文件　`native/old.wasm`

```text
定位本仓库 tools/rea/测试样例.zip，在临时目录解压，以下路径均相对于包内 samples/。
本项输入按顺序为 native/old.wasm。
请用 rea 的 inspect_wasm_artifact 验证我提供的 native/old.wasm，列出模块导入和导出的名称。
```

<a id="item-94"></a>

#### 94 · `inspect_gpu_code_objects`

样例文件　`native/sample.cubin`

```text
定位本仓库 tools/rea/测试样例.zip，在临时目录解压，以下路径均相对于包内 samples/。
本项输入按顺序为 native/sample.cubin。
请用 rea 的 inspect_gpu_code_objects 盘点我提供的 native/sample.cubin，列出可识别的 GPU 目标架构。
```

<a id="item-95"></a>

#### 95 · `inspect_model_artifact`

样例文件　`native/weights.safetensors`

```text
定位本仓库 tools/rea/测试样例.zip，在临时目录解压，以下路径均相对于包内 samples/。
本项输入按顺序为 native/weights.safetensors。
请用 rea 的 inspect_model_artifact 读取我提供的 native/weights.safetensors，列出每个张量的名称、数据类型和形状。
```

### 文件、应用包与数据库

<a id="item-98"></a>

#### 98 · `inspect_desktop_application`

样例文件　`apple/Demo.app`

```text
定位本仓库 tools/rea/测试样例.zip，在临时目录解压，以下路径均相对于包内 samples/。
本项输入按顺序为 apple/Demo.app。
请用 rea 的 inspect_desktop_application 检查我提供的桌面应用安装目录，根据文件和元数据列出可能使用的运行时。
```

<a id="item-99"></a>

#### 99 · `audit_release_exposure`

样例文件　`apple/Demo.app`

```text
定位本仓库 tools/rea/测试样例.zip，在临时目录解压，以下路径均相对于包内 samples/。
本项输入按顺序为 apple/Demo.app。
请用 rea 的 audit_release_exposure 检查我自己的 apple/Demo.app 发布包，列出可从成品静态读取的信息及对应文件。
```

<a id="item-100"></a>

#### 100 · `inspect_sqlite_database`

样例文件　`data/demo.sqlite`

```text
定位本仓库 tools/rea/测试样例.zip，在临时目录解压，以下路径均相对于包内 samples/。
本项输入按顺序为 data/demo.sqlite。
请用 rea 的 inspect_sqlite_database 从我提供的 data/demo.sqlite 快照的 products 表中读取前五行，只显示 id 和 name 两列。
```

### 证据、版本差异与重建验证

<a id="item-103"></a>

#### 103 · `import_evidence_bundle`

样例文件　`evidence/members.json`

```text
定位本仓库 tools/rea/测试样例.zip，在临时目录解压，以下路径均相对于包内 samples/。
本项输入按顺序为 evidence/members.json。导入到全新测试会话。
请用 rea 的 import_evidence_bundle 校验我提供的 evidence/members.json，并把通过校验的记录导入当前测试会话。
```

<a id="item-104"></a>

#### 104 · `compare_bundles`

样例文件　`evidence/empty.json`、`evidence/comparison.json`

```text
定位本仓库 tools/rea/测试样例.zip，在临时目录解压，以下路径均相对于包内 samples/。
本项输入按顺序为 evidence/empty.json 和 evidence/comparison.json。旧包选 empty.json，新包选 comparison.json。
请用 rea 的 compare_bundles 对比我提供的 evidence/empty.json 和 evidence/comparison.json，概括证据记录的差异。
```

<a id="item-109"></a>

#### 109 · `build_reconstruction_obligation_ledger`

样例文件　`evidence/ledger.json`

```text
定位本仓库 tools/rea/测试样例.zip，在临时目录解压，以下路径均相对于包内 samples/。
本项输入按顺序为 evidence/ledger.json。读取 JSON，将顶层对象作为工具参数。
请用 rea 的 build_reconstruction_obligation_ledger 根据我提供的 REA 证据包、已审阅事项和重建清单，列出仍需验证的事项。
```

<a id="item-110"></a>

#### 110 · `evaluate_reconstruction_coverage`

样例文件　`evidence/coverage.json`

```text
定位本仓库 tools/rea/测试样例.zip，在临时目录解压，以下路径均相对于包内 samples/。
本项输入按顺序为 evidence/coverage.json。读取 JSON，将顶层对象作为工具参数。
请用 rea 的 evaluate_reconstruction_coverage 使用我提供的覆盖评估输入，检查 replacement.cli 这个边界还有哪些要求缺少验证证据。
```

## 58 条会话或前序结果示例

[查看上轮出现 MCP 报错的 11 条指令复测结果](./11条指令MCP零报错复测.md)

[查看这 58 条指令在全新对话里的首轮和复测结果](./58条准备指令全新对话实测.md)

### 网页、浏览器与 Electron

<a id="item-6"></a>

#### 6 · `inspect_web_page`

```text
定位本仓库 tools/rea/测试样例.zip，在临时目录解压，以下路径均相对于包内 samples/。
用 Python 3 在独立的终端任务启动 live/start.py browser，保持进程运行，读取它打印的第一行 JSON，把其中全部字段作为本次工具的连接参数。完成后停止这次启动的进程。
请用 rea 的 inspect_web_page 检查我通过本机 CDP 连接并指定的测试页，告诉我页面标题和加载了哪些脚本。
```

<a id="item-7"></a>

#### 7 · `inspect_web_event_listeners`

```text
定位本仓库 tools/rea/测试样例.zip，在临时目录解压，以下路径均相对于包内 samples/。
用 Python 3 在独立的终端任务启动 live/start.py browser，保持进程运行，读取它打印的第一行 JSON，把其中全部字段作为本次工具的连接参数。完成后停止这次启动的进程。
请用 rea 的 inspect_web_event_listeners 查看指定 CDP 测试页上 #submit 按钮直接注册的监听器，列出事件类型及可定位的回调脚本。
```

<a id="item-8"></a>

#### 8 · `capture_web_screenshot`

```text
定位本仓库 tools/rea/测试样例.zip，在临时目录解压，以下路径均相对于包内 samples/。
用 Python 3 在独立的终端任务启动 live/start.py browser，保持进程运行，读取它打印的第一行 JSON，把其中全部字段作为本次工具的连接参数。完成后停止这次启动的进程。
请用 rea 的 capture_web_screenshot 为我指定的本机 CDP 测试页截一张当前可见区域的 PNG。
```

<a id="item-9"></a>

#### 9 · `compare_web_screenshots`

```text
定位本仓库 tools/rea/测试样例.zip，在临时目录解压，以下路径均相对于包内 samples/。
读取 web/screenshots.json，将 before 和 after 两份截图按文件内的实际字段名及顺序作为比较参数，保留像素和校验字段。
请用 rea 的 compare_web_screenshots 比较本对话中先后取得的两份 REA 网页截图，给出发生变化的像素占比。
```

<a id="item-10"></a>

#### 10 · `observe_web_session`

```text
定位本仓库 tools/rea/测试样例.zip，在临时目录解压，以下路径均相对于包内 samples/。
用 Python 3 在独立的终端任务启动 live/start.py browser，保持进程运行，读取它打印的第一行 JSON，把其中全部字段作为本次工具的连接参数。完成后停止这次启动的进程。 观察时长填 10000 毫秒；页面可以静置。
请用 rea 的 observe_web_session 在我操作指定的本机 CDP 测试页时观察 10 秒，按顺序概括记录到的页面事件。
```

<a id="item-11"></a>

#### 11 · `compare_web_captures`

```text
定位本仓库 tools/rea/测试样例.zip，在临时目录解压，以下路径均相对于包内 samples/。
读取 web/web-scenario1.json 和 web/web-scenario2.json 的 JSON 内容，依次传入 before_scenario 和 after_scenario。
请用 rea 的 compare_web_captures 比较我提供的改版前后两份同类 REA 浏览器场景记录，列出有变化的页面资源。
```

<a id="item-12"></a>

#### 12 · `discover_webmcp_tools`

```text
定位本仓库 tools/rea/测试样例.zip，在临时目录解压，以下路径均相对于包内 samples/。
用 Python 3 在独立的终端任务启动 live/start.py browser，保持进程运行，读取它打印的第一行 JSON，把其中全部字段作为本次工具的连接参数。完成后停止这次启动的进程。 样例页未注册 WebMCP 工具，报告实际条数即可。
请用 rea 的 discover_webmcp_tools 查看我指定的本机 CDP 测试页声明了哪些 WebMCP 工具，给出名称和参数。
```

<a id="item-14"></a>

#### 14 · `inspect_electron_page`

```text
定位本仓库 tools/rea/测试样例.zip，在临时目录解压，以下路径均相对于包内 samples/。
使用独立的 Electron 运行时。Apple 芯片的 Mac 若没有 electron，可将官方 https://github.com/electron/electron/releases/download/v45.4.1/electron-v45.4.1-darwin-arm64.zip 下载到临时目录。若官方直连超时，可从 https://registry.npmmirror.com/-/binary/electron/v45.4.1/electron-v45.4.1-darwin-arm64.zip 续传同一发行文件。用 shasum -a 256 核对 d080c3b05a01bd16137f2c12ab9ebf083c577757fe846844ba325bafa8e8bdf4，再用 ditto -xk 解压，将 ELECTRON_BIN 指向解压后的 Electron.app/Contents/MacOS/Electron。用 Python 3 在独立的终端任务启动 live/start.py electron，保持进程运行，读取它打印的第一行 JSON，把其中全部字段作为本次工具的连接参数。完成后停止这次启动的进程。
请用 rea 的 inspect_electron_page 使用我提供的本机 CDP 端点和目标 ID，查看 Electron 测试应用中本地文件页的主框架 URL。若返回 frames[].file_path，取 parent_frame_id 为空的那一帧，并把该路径转为 file URL，注明这是从工具返回路径换算的。
```

### JavaScript、源码映射与 API

<a id="item-17"></a>

#### 17 · `trace_application_feature`

```text
定位本仓库 tools/rea/测试样例.zip，在临时目录解压，以下路径均相对于包内 samples/。
用 analyze_javascript_application 分析 js/app.asar，detail 填 complete，从返回顶层取 evidence_id 作为应用图ID。
调用 trace_application_feature 时使用下面的 JSON 结构，把尖括号占位符替换为本次实际值。
{"application": {"kind": "retained-evidence", "evidence_id": "<应用图ID>"}, "seed": {"kind": "module", "value": "renderer.js", "match": "exact"}, "direction": "outgoing"}
请用 rea 的 trace_application_feature 在刚生成的 JavaScript 应用图中，以 renderer.js 模块为起点追踪它关联的功能。
```

<a id="item-18"></a>

#### 18 · `trace_javascript_semantics`

```text
定位本仓库 tools/rea/测试样例.zip，在临时目录解压，以下路径均相对于包内 samples/。
用 analyze_javascript_application 分析 js/app.asar，detail 填 complete，从返回顶层取 evidence_id 作为应用图ID。从该结果的语义图取 profile.js 中 getProfile 的 return 节点，把实际的 jsrg_node_ 标识作为返回节点ID。
调用 trace_javascript_semantics 时使用下面的 JSON 结构，把尖括号占位符替换为本次实际值。
{"application": {"kind": "retained-evidence", "evidence_id": "<应用图ID>"}, "query": {"seed": {"kind": "semantic-node", "node_id": "<返回节点ID>"}, "direction": "backward-provenance"}}
请用 rea 的 trace_javascript_semantics 使用我选中的语义节点 ID，在本对话的 JavaScript 应用图中向后追溯它的值来自哪里。
```

<a id="item-22"></a>

#### 22 · `compare_source_to_bundle`

```text
定位本仓库 tools/rea/测试样例.zip，在临时目录解压，以下路径均相对于包内 samples/。
用 analyze_javascript_application 分析 js/app.asar，detail 填 complete，从返回顶层取 evidence_id 作为应用图ID。取 js/reference.json 解压后的绝对路径。
调用 compare_source_to_bundle 时使用下面的 JSON 结构，把尖括号占位符替换为本次实际值。
{"reference": {"kind": "file", "path": "<reference.json绝对路径>"}, "application": {"kind": "retained-evidence", "evidence_id": "<应用图ID>"}}
请用 rea 的 compare_source_to_bundle 将我提供的历史源码图 HistoricalSourceGraph 与本对话的打包应用图比对，列出修改过的模块。
```

<a id="item-23"></a>

#### 23 · `compare_application_versions`

```text
定位本仓库 tools/rea/测试样例.zip，在临时目录解压，以下路径均相对于包内 samples/。
对 js/v1 和 js/v2 分别调用 analyze_javascript_application，detail 填 summary。从各自 normalized_result.parent_evidence_id 取旧版ID和新版ID。
调用 compare_application_versions 时使用下面的 JSON 结构，把尖括号占位符替换为本次实际值。
{"left": {"kind": "retained-evidence", "evidence_id": "<旧版ID>"}, "right": {"kind": "retained-evidence", "evidence_id": "<新版ID>"}}
请用 rea 的 compare_application_versions 使用本会话中新旧两份 JavaScript 分析摘要各自的 parent_evidence_id 对比应用图，分别列出新增和删除的模块。
```

<a id="item-24"></a>

#### 24 · `compare_javascript_export_shapes`

```text
定位本仓库 tools/rea/测试样例.zip，在临时目录解压，以下路径均相对于包内 samples/。
对 js/v1 和 js/v2 分别调用 analyze_javascript_application，detail 填 summary。从各自 normalized_result.parent_evidence_id 取旧版ID和新版ID。
调用 compare_javascript_export_shapes 时使用下面的 JSON 结构，把尖括号占位符替换为本次实际值。
{"left": {"kind": "retained-evidence", "evidence_id": "<旧版ID>"}, "right": {"kind": "retained-evidence", "evidence_id": "<新版ID>"}, "left_export_name": "getProfile", "right_export_name": "getProfile", "left_module_path": "profile.js", "right_module_path": "profile.js"}
请用 rea 的 compare_javascript_export_shapes 使用新旧 JavaScript 分析摘要各自的 parent_evidence_id，比较两版 profile.js 中 getProfile 的静态返回属性。
```

<a id="item-25"></a>

#### 25 · `observe_javascript_runtime`

```text
定位本仓库 tools/rea/测试样例.zip，在临时目录解压，以下路径均相对于包内 samples/。
用 Python 3 在独立的终端任务启动 live/start.py node，保持进程运行，读取它打印的第一行 JSON，把其中全部字段作为本次工具的连接参数。完成后停止这次启动的进程。
请用 rea 的 observe_javascript_runtime 使用我提供的本机 V8 Inspector 端点和目标 ID，列出 Node 测试进程已载入的脚本。
```

<a id="item-26"></a>

#### 26 · `reconcile_javascript_runtime`

```text
定位本仓库 tools/rea/测试样例.zip，在临时目录解压，以下路径均相对于包内 samples/。
用 Python 3 启动 live/start.py node，保持它运行。将首行 JSON 原样传给 observe_javascript_runtime，取该观测的证据ID。用 analyze_javascript_application 分析 node 目录，detail 填 summary，取 normalized_result.parent_evidence_id 作为应用图ID。完成比对后停止本次启动的 Node 测试进程。
调用 reconcile_javascript_runtime 时使用下面的 JSON 结构，把尖括号占位符替换为本次实际值。
{"static_layers": [{"role": "application", "analysis": {"kind": "retained-evidence", "evidence_id": "<应用图ID>"}}], "runtime_observations": [{"kind": "retained-evidence", "evidence_id": "<观测的证据ID>"}]}
请用 rea 的 reconcile_javascript_runtime 对齐本对话的 JavaScript 静态应用图和已有的 V8 观测记录，列出两边都能确认的脚本。
```

<a id="item-27"></a>

#### 27 · `compare_static_and_observed_endpoints`

```text
定位本仓库 tools/rea/测试样例.zip，在临时目录解压，以下路径均相对于包内 samples/。
分别用以下参数准备两份摘要，路径换成本次解压的绝对路径。
analyze_javascript_application 用 {"input_path":"<js/endpoint目录>","detail":"summary"}。
inspect_web_network_capture 用 {"capture_path":"<web/demo.har文件>","format":"har","detail":"summary"}。
依次取两份摘要的 normalized_result.parent_evidence_id，作为应用图ID和抓包ID。
调用 compare_static_and_observed_endpoints 时使用下面的 JSON 结构，把尖括号占位符替换为本次实际值。
{"application": {"kind": "retained-evidence", "evidence_id": "<应用图ID>"}, "capture": {"kind": "retained-evidence", "evidence_id": "<抓包ID>"}, "origin": "https://fixture.invalid", "detail": "complete"}
请用 rea 的 compare_static_and_observed_endpoints 核对本对话的应用图与同一测试应用的 HAR 分析结果，列出代码声明且抓包中出现过的接口。
```

### Android、ADB、Flutter 与鸿蒙

<a id="item-37"></a>

#### 37 · `project_android_application_graph`

```text
定位本仓库 tools/rea/测试样例.zip，在临时目录解压，以下路径均相对于包内 samples/。
用 open_binary 打开 mobile/toy.apk，再调用 inspect_artifact 获得嵌套清单。把刚返回的完整证据作为 retained-evidence 放进 inventory_evidence 数组。
请用 rea 的 project_android_application_graph 根据本对话里 mobile/toy.apk 的嵌套文件清单证据，列出组件路径及运行时线索。
```

<a id="item-40"></a>

#### 40 · `project_harmony_application_graph`

```text
定位本仓库 tools/rea/测试样例.zip，在临时目录解压，以下路径均相对于包内 samples/。
用 open_binary 打开 mobile/harmony.app，再调用 inspect_artifact 获得嵌套清单。把刚返回的完整证据作为 retained-evidence 放进 inventory_evidence 数组。
请用 rea 的 project_harmony_application_graph 根据本对话里 mobile/harmony.app 鸿蒙 App Pack 的嵌套清单证据，列出子包名称及路径。
```

### Apple 应用、Swift 与 Objective-C

<a id="item-41"></a>

#### 41 · `project_apple_application_graph`

```text
定位本仓库 tools/rea/测试样例.zip，在临时目录解压，以下路径均相对于包内 samples/。
用 open_binary 打开 mobile/toy.ipa，再调用 inspect_artifact 获得嵌套清单。把刚返回的完整证据作为 retained-evidence 放进 inventory_evidence 数组。
请用 rea 的 project_apple_application_graph 根据本对话里 mobile/toy.ipa 的嵌套清单证据，列出主应用和内嵌扩展所在的目录。
```

<a id="item-43"></a>

#### 43 · `decode_interface_builder`

```text
定位本仓库 tools/rea/测试样例.zip，在临时目录解压，以下路径均相对于包内 samples/。
使用 open_bundle_resources 打开 apple/Demo.app，保持该资源会话。 编译界面位于 Contents/Resources/Demo.storyboardc。
请用 rea 的 decode_interface_builder 查看当前已打开的 Demo.app 中编译后的 storyboard，列出可识别的界面层级和控件连接。
```

<a id="item-44"></a>

#### 44 · `inspect_asset_catalog`

```text
定位本仓库 tools/rea/测试样例.zip，在临时目录解压，以下路径均相对于包内 samples/。
在新的临时目录复制 apple/Demo.app。把本机 /System/Applications/Calculator.app/Contents/Resources/Assets.car 复制到样例副本的 Contents/Resources/Assets.car。用 open_bundle_resources 打开该副本。接下来调用 inspect_asset_catalog 时，offset 填 0，limit 填 10。若本机缺少此系统文件，报告具体路径。
请用 rea 的 inspect_asset_catalog 查看当前已打开的 Demo.app 的资源目录，从第一项起列出最多十个资源条目。
```

<a id="item-45"></a>

#### 45 · `inspect_keyed_archive`

```text
定位本仓库 tools/rea/测试样例.zip，在临时目录解压，以下路径均相对于包内 samples/。
使用 open_bundle_resources 打开 apple/Demo.app，保持该资源会话。 使用包内相对路径 Contents/Resources/Model.plist。
请用 rea 的 inspect_keyed_archive 读取当前 Demo.app 中的 Contents/Resources/Model.plist 键值归档，列出根对象及其引用的类。
```

<a id="item-46"></a>

#### 46 · `inspect_plist`

```text
定位本仓库 tools/rea/测试样例.zip，在临时目录解压，以下路径均相对于包内 samples/。
使用 open_bundle_resources 打开 apple/Demo.app，保持该资源会话。 使用包内相对路径 Contents/Info.plist。
请用 rea 的 inspect_plist 读取当前 Demo.app 的 Contents/Info.plist，告诉我 CFBundleIdentifier 和 CFBundleVersion。
```

<a id="item-47"></a>

#### 47 · `inspect_macho`

```text
定位本仓库 tools/rea/测试样例.zip，在临时目录解压，以下路径均相对于包内 samples/。
用 open_binary 打开 native/universal，使用自动识别，确认返回已打开，再在同一会话继续。
请用 rea 的 inspect_macho 在已用 open_binary 成功打开的 Mach-O 样例中，列出切片架构和加载命令。
```

<a id="item-48"></a>

#### 48 · `inspect_signature`

```text
定位本仓库 tools/rea/测试样例.zip，在临时目录解压，以下路径均相对于包内 samples/。
用 open_binary 打开 native/universal，使用自动识别，确认返回已打开，再在同一会话继续。
请用 rea 的 inspect_signature 读取刚成功打开的 Mach-O 样例，列出它的签名身份和声明的授权项。
```

<a id="item-50"></a>

#### 50 · `demangle_swift`

```text
定位本仓库 tools/rea/测试样例.zip，在临时目录解压，以下路径均相对于包内 samples/。
用 open_binary 打开 native/types-demo。它包含 AccountSample 和 DemoViewController，打开成功后在同一会话继续。
请用 rea 的 demangle_swift 在已打开的 Mach-O 测试目标中，把 Swift 符号 $s4Test3fooyyF 还原成可读名称。
```

<a id="item-51"></a>

#### 51 · `analyze_swift_types`

```text
定位本仓库 tools/rea/测试样例.zip，在临时目录解压，以下路径均相对于包内 samples/。
用 open_binary 打开 native/types-demo。它包含 AccountSample 和 DemoViewController，打开成功后在同一会话继续。
请用 rea 的 analyze_swift_types 在当前打开的 Swift 测试程序里查找名称含 Account 的类。
```

<a id="item-52"></a>

#### 52 · `get_objc_classes`

```text
定位本仓库 tools/rea/测试样例.zip，在临时目录解压，以下路径均相对于包内 samples/。
用 open_binary 打开 native/types-demo。它包含 AccountSample 和 DemoViewController，打开成功后在同一会话继续。
请用 rea 的 get_objc_classes 在当前打开的测试程序中列出名称含 ViewController 的 Objective-C 类。
```

<a id="item-53"></a>

#### 53 · `get_objc_protocols`

```text
定位本仓库 tools/rea/测试样例.zip，在临时目录解压，以下路径均相对于包内 samples/。
用 open_binary 打开 native/types-demo。它包含 AccountSample 和 DemoViewController，打开成功后在同一会话继续。
请用 rea 的 get_objc_protocols 列出当前分析后端在已打开的测试程序中识别到的 Objective-C 协议；如果列表为空，就报告零项。
```

### 原生二进制、符号与分析会话

<a id="item-56"></a>

#### 56 · `close_binary`

```text
定位本仓库 tools/rea/测试样例.zip，在临时目录解压，以下路径均相对于包内 samples/。
用 open_binary 以 ghidra 后端打开 native/demo 的临时副本，等待分析完成。
请用 rea 的 close_binary 关闭本对话当前打开的测试二进制，并报告关闭结果。
```

<a id="item-57"></a>

#### 57 · `binary_overview`

```text
定位本仓库 tools/rea/测试样例.zip，在临时目录解压，以下路径均相对于包内 samples/。
用 open_binary 以 ghidra 后端打开 native/demo 的临时副本，等待分析完成。
请用 rea 的 binary_overview 汇总当前打开的测试程序，告诉我后端已识别多少个函数和字符串。
```

<a id="item-58"></a>

#### 58 · `list_architectures`

```text
定位本仓库 tools/rea/测试样例.zip，在临时目录解压，以下路径均相对于包内 samples/。
用 open_binary 打开 native/universal，使用自动识别，确认返回已打开，再在同一会话继续。
请用 rea 的 list_architectures 在刚成功打开的通用 Mach-O 文件中枚举架构，逐项给出工具识别的架构名。
```

<a id="item-59"></a>

#### 59 · `list_documents`

```text
定位本仓库 tools/rea/测试样例.zip，在临时目录解压，以下路径均相对于包内 samples/。
用 open_binary 以 ghidra 后端打开 native/demo 的临时副本，等待分析完成。
请用 rea 的 list_documents 列出当前分析后端可见的文档，并告诉我哪些对应刚打开的测试程序。
```

<a id="item-60"></a>

#### 60 · `list_segments`

```text
定位本仓库 tools/rea/测试样例.zip，在临时目录解压，以下路径均相对于包内 samples/。
用 open_binary 以 ghidra 后端打开 native/demo 的临时副本，等待分析完成。
请用 rea 的 list_segments 列出当前测试程序的内存段名称以及各段的起止地址。
```

<a id="item-61"></a>

#### 61 · `list_procedures`

```text
定位本仓库 tools/rea/测试样例.zip，在临时目录解压，以下路径均相对于包内 samples/。
用 open_binary 以 ghidra 后端打开 native/demo 的临时副本，等待分析完成。
请用 rea 的 list_procedures 列出当前测试程序中已识别的函数，先展示前十个名称和地址。
```

<a id="item-62"></a>

#### 62 · `search_procedures`

```text
定位本仓库 tools/rea/测试样例.zip，在临时目录解压，以下路径均相对于包内 samples/。
用 open_binary 以 ghidra 后端打开 native/demo 的临时副本，等待分析完成。
请用 rea 的 search_procedures 在当前测试程序中按字面、不区分大小写搜索 main，列出匹配的函数。
```

<a id="item-63"></a>

#### 63 · `list_names`

```text
定位本仓库 tools/rea/测试样例.zip，在临时目录解压，以下路径均相对于包内 samples/。
用 open_binary 以 ghidra 后端打开 native/demo 的临时副本，等待分析完成。
请用 rea 的 list_names 列出当前测试程序的已命名符号，先展示十组地址和名称。
```

<a id="item-64"></a>

#### 64 · `address_name`

```text
定位本仓库 tools/rea/测试样例.zip，在临时目录解压，以下路径均相对于包内 samples/。
用 open_binary 以 ghidra 后端打开 native/demo 的临时副本，等待分析完成。 调用 list_procedures，从返回列表取第一个函数的起始 address。
请用 rea 的 address_name 查询上一条函数列表中第一个函数的起始地址，告诉我它的符号名。
```

<a id="item-65"></a>

#### 65 · `inspect_address_context`

```text
定位本仓库 tools/rea/测试样例.zip，在临时目录解压，以下路径均相对于包内 samples/。
用 open_binary 以 ghidra 后端打开 native/demo 的临时副本，等待分析完成。 调用 list_procedures，从返回列表取第一个函数的起始 address。
请用 rea 的 inspect_address_context 检查上一条函数列表中第一个函数的起始地址，给出所属函数和可读取的注释。
```

<a id="item-66"></a>

#### 66 · `set_address_name`

```text
定位本仓库 tools/rea/测试样例.zip，在临时目录解压，以下路径均相对于包内 samples/。
用 open_binary 以 ghidra 后端打开 native/demo 的临时副本，等待分析完成。 调用 list_procedures，从返回列表取第一个函数的起始 address。
请用 rea 的 set_address_name 将我选中的测试函数起始地址重命名为 demo_entry，并告诉我改动的地址。
```

<a id="item-67"></a>

#### 67 · `set_addresses_names`

```text
定位本仓库 tools/rea/测试样例.zip，在临时目录解压，以下路径均相对于包内 samples/。
将 native/demo 的临时副本用 open_binary 打开，provider_id 填 ghidra。调用 list_procedures，按顺序取前两个不同函数的起始地址作为下面的键。保留改名返回的回读结果，最后用空参数 {} 调用 close_binary 关闭本次临时目标。
调用 set_addresses_names 时使用下面的 JSON 结构，把尖括号占位符替换为本次实际值。
{"names": {"<第一个地址>": "demo_load", "<第二个地址>": "demo_save"}}
请用 rea 的 set_addresses_names 将我依次选中的两个不同测试函数地址分别命名为 demo_load 和 demo_save。
```

### 编程语言、托管代码与计算模型

<a id="item-87"></a>

#### 87 · `compare_managed_members`

```text
定位本仓库 tools/rea/测试样例.zip，在临时目录解压，以下路径均相对于包内 samples/。
先 import_evidence_bundle 导入 evidence/members.json，再读取 evidence/args-87.json 作为本项参数；其中的 ID 对应这个样例包中的成员证据。
请用 rea 的 compare_managed_members 比较我提供的新旧两份 REA 托管成员证据，列出能够匹配的成员及其签名变化。
```

<a id="item-89"></a>

#### 89 · `verify_managed_native_boundaries`

```text
定位本仓库 tools/rea/测试样例.zip，在临时目录解压，以下路径均相对于包内 samples/。
用 inspect_managed_native_boundaries 读 native/Interop.dll，取声明证据ID。再用 open_binary 打开 native/libdemo.dylib，调用 inspect_macho 取得导出证据ID。直接在当前会话引用这两份记录。
调用 verify_managed_native_boundaries 时使用下面的 JSON 结构，把尖括号占位符替换为本次实际值。
{"managed_boundaries": {"kind": "retained-evidence", "evidence_id": "<声明证据ID>"}, "native_observations": [{"kind": "retained-evidence", "evidence_id": "<导出证据ID>"}]}
请用 rea 的 verify_managed_native_boundaries 用本对话的 P/Invoke 声明证据和对应动态库的 inspect_macho 导出证据，逐项核对入口名并说明匹配依据。
```

<a id="item-90"></a>

#### 90 · `project_managed_application_graph`

```text
定位本仓库 tools/rea/测试样例.zip，在临时目录解压，以下路径均相对于包内 samples/。
先 import_evidence_bundle 导入 evidence/members.json，再读取 evidence/args-90.json 作为本项参数；其中的 ID 对应这个样例包中的成员证据。
请用 rea 的 project_managed_application_graph 使用我提供的 REA 托管成员证据生成 .NET 应用关系图，列出其中可识别的类型与成员。
```

<a id="item-93"></a>

#### 93 · `compare_wasm_interfaces`

```text
定位本仓库 tools/rea/测试样例.zip，在临时目录解压，以下路径均相对于包内 samples/。
用 inspect_wasm_artifact 依次读取 native/old.wasm 和 native/new.wasm，detail 均填 complete，各取顶层 evidence_id 作为旧版ID和新版ID。
调用 compare_wasm_interfaces 时使用下面的 JSON 结构，把尖括号占位符替换为本次实际值。
{"left": {"kind": "retained-evidence", "evidence_id": "<旧版ID>"}, "right": {"kind": "retained-evidence", "evidence_id": "<新版ID>"}, "scope": "exports"}
请用 rea 的 compare_wasm_interfaces 比较本对话中两份 WASM 模块检查结果，列出新增、移除或签名变化的导出项。
```

### 文件、应用包与数据库

<a id="item-96"></a>

#### 96 · `inspect_artifact`

```text
定位本仓库 tools/rea/测试样例.zip，在临时目录解压，以下路径均相对于包内 samples/。
先用 open_binary 打开 data/demo.zip，保持当前归档会话。
请用 rea 的 inspect_artifact 检查当前已打开的 demo.zip，列出内部文件的路径和条目标识。
```

<a id="item-97"></a>

#### 97 · `extract_artifact`

```text
定位本仓库 tools/rea/测试样例.zip，在临时目录解压，以下路径均相对于包内 samples/。
先用 open_binary 打开 data/demo.zip，保持当前归档会话。 再用 inspect_artifact 取 README.txt 的 occurrence_id，选一个新的空输出目录作为 output_root。
请用 rea 的 extract_artifact 按上一条清单中 README.txt 的条目标识，只把这个文件解包到工作区新目录 demo-extract。
```

### 证据、版本差异与重建验证

<a id="item-105"></a>

#### 105 · `compare_artifacts`

```text
定位本仓库 tools/rea/测试样例.zip，在临时目录解压，以下路径均相对于包内 samples/。
用 import_evidence_bundle 导入 evidence/comparison.json。 读取 evidence/args-105.json，把其中的 left 和 right 用作本工具参数；顺序已经按旧版、新版排好。
请用 rea 的 compare_artifacts 比较本对话中旧版和新版安装包的两份文件清单证据，列出新增和内容变化的文件。
```

<a id="item-106"></a>

#### 106 · `compare_process_captures`

```text
定位本仓库 tools/rea/测试样例.zip，在临时目录解压，以下路径均相对于包内 samples/。
用 import_evidence_bundle 导入 evidence/comparison.json。 读取 evidence/args-106.json，把其中的 left 和 right 用作本工具参数；顺序已经按旧版、新版排好。
请用 rea 的 compare_process_captures 对比我提供的同一测试命令前后两次的 REA 进程记录，告诉我终端输出有什么变化。
```

<a id="item-107"></a>

#### 107 · `find_changed_behavior`

```text
定位本仓库 tools/rea/测试样例.zip，在临时目录解压，以下路径均相对于包内 samples/。
用 import_evidence_bundle 导入 evidence/comparison.json。 用 evidence/args-105.json 内的参数运行 compare_artifacts，记下这次返回的 evidence_id。用 evidence/args-106.json 内的参数运行 compare_process_captures，记下这次返回的 evidence_id。读取 evidence/args-107.json，把其中形如 {"ref":"编号/evidence_id"} 的对象替换成相应步骤刚返回的 ID 字符串，再提交整个参数对象。
请用 rea 的 find_changed_behavior 汇总本对话中已有的产物和进程比较证据，指出哪些行为有可核实的变化。
```

<a id="item-108"></a>

#### 108 · `correlate_static_and_runtime`

```text
定位本仓库 tools/rea/测试样例.zip，在临时目录解压，以下路径均相对于包内 samples/。
用 import_evidence_bundle 导入 evidence/comparison.json。 用 evidence/args-106.json 内的参数运行 compare_process_captures，记下这次返回的 evidence_id。读取 evidence/args-108.json，把其中形如 {"ref":"编号/evidence_id"} 的对象替换成相应步骤刚返回的 ID 字符串，再提交整个参数对象。
请用 rea 的 correlate_static_and_runtime 使用本对话的函数比较和进程比较证据，按旧版对应旧版、新版对应新版，核对该函数的变化是否伴随终端输出变化。
```

<a id="item-111"></a>

#### 111 · `verify_reconstruction`

```text
定位本仓库 tools/rea/测试样例.zip，在临时目录解压，以下路径均相对于包内 samples/。
用 import_evidence_bundle 导入 evidence/comparison.json。 用 evidence/args-106.json 内的参数运行 compare_process_captures，记下这次返回的 evidence_id。读取 evidence/args-111.json，把其中形如 {"ref":"编号/evidence_id"} 的对象替换成相应步骤刚返回的 ID 字符串，再提交整个参数对象。
请用 rea 的 verify_reconstruction 按我提供的重建规格和本会话的证据，核验两版测试命令的终端输出是否满足规格中的一致性要求。
```

<a id="item-114"></a>

#### 114 · `update_unknown`

```text
定位本仓库 tools/rea/测试样例.zip，在临时目录解压，以下路径均相对于包内 samples/。
用 record_unknown 登记一个新的测试问题：“同一输入能否产生相同摘要？”domain 填“离线输出”，severity 填 medium，required_authority 填 controlled-replay，required_confidence 填 observed，无指定环境，relationships 和 recommended_probes 为空数组。 从返回结果取 unknown_id、revision 和其余当前字段；用该 revision 作为 expected_revision，仅将 status 改为 investigating。
请用 rea 的 update_unknown 使用上一条问题的 ID 和当前修订号，将该问题的处理状态更新为调查中。
```

<a id="item-115"></a>

#### 115 · `verify_unknown_resolution`

```text
定位本仓库 tools/rea/测试样例.zip，在临时目录解压，以下路径均相对于包内 samples/。
用 record_unknown 登记一个新的测试问题：“同一输入能否产生相同摘要？”domain 填“离线输出”，severity 填 medium，required_authority 填 controlled-replay，required_confidence 填 observed，无指定环境，relationships 和 recommended_probes 为空数组。 使用该 unknown_id；保留当前证据条件，按实际返回说明是否还缺少受控重放。
请用 rea 的 verify_unknown_resolution 根据我选中的问题 ID 和当前证据，说明它是否满足结案条件。
```

<a id="item-116"></a>

#### 116 · `export_environment_bundle`

```text
定位本仓库 tools/rea/测试样例.zip，在临时目录解压，以下路径均相对于包内 samples/。
用 inspect_web_network_capture 按 har 格式读取 web/demo.har，取完整记录的 evidence_id 作为抓包ID。在工作区新建专用目录，选其中尚不存在的 demo-environment 作为导出绝对路径。
调用 export_environment_bundle 时使用下面的 JSON 结构，把尖括号占位符替换为本次实际值。
{"name": "offline-demo", "source": {"kind": "retained-evidence", "evidence_id": "<抓包ID>"}, "output_directory": "<导出绝对路径>"}
请用 rea 的 export_environment_bundle 用本对话中合成 HAR 的分析证据，把测试环境包导出到工作区新目录 demo-environment。
```

<a id="item-117"></a>

#### 117 · `reset_investigation`

```text
定位本仓库 tools/rea/测试样例.zip，在临时目录解压，以下路径均相对于包内 samples/。
在专用的新 Codex 测试对话里运行这一条。先用 get_evidence_bundle 和 list_unknowns 确认两者均为空，有其他数据就停止。用 inspect_web_network_capture 读取 web/demo.har，让临时调查包含一份证据。在新建的空工作目录中选 before-reset.json，调用时 overwrite 设为 false。完成后核对备份含该记录，再确认本次调查为空。
请用 rea 的 reset_investigation 将当前临时测试调查的证据保存到工作区新文件 before-reset.json，再清空这次调查的证据和问题历史。
```

### 工作指南、设置与结果浏览

<a id="item-120"></a>

#### 120 · `read_guidance_section`

```text
定位本仓库 tools/rea/测试样例.zip，在临时目录解压，以下路径均相对于包内 samples/。
调用 search_guidance 搜索 JavaScript module，limit 填 3。取首项实际返回的完整 locator，原样传给 read_guidance_section。
请用 rea 的 read_guidance_section 用上一条指南搜索结果中第一项的定位信息读取该节，并概括操作步骤。
```

<a id="item-123"></a>

#### 123 · `inspect_analysis_view`

```text
定位本仓库 tools/rea/测试样例.zip，在临时目录解压，以下路径均相对于包内 samples/。
分别用 analyze_javascript_application 分析 js/endpoint 目录、用 inspect_web_network_capture 按 HAR 格式读取 web/demo.har。保留这两项完整证据的 ID；摘要结果取 parent_evidence_id。 接着调用 compare_static_and_observed_endpoints，传入 application、capture 和 origin=https://fixture.invalid，detail 选 summary。从返回的 normalized_result 取 parent_evidence_id 作为下一步的 source。
请用 rea 的 inspect_analysis_view 使用刚得到的接口对比摘要中的 parent_evidence_id，在 endpoint-comparison 视图的 static-endpoints 集合中读取前十条接口记录。
```
