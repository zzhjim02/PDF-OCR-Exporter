# PDF OCR文本提取大师

一个专业的PDF OCR文本提取工具,支持批量处理、多线程并行、智能跳过等功能。PDF-OCR-Exporter-lite的升级版

## 版权信息

**作者**: 浮生＆2cm

**单位**: 湖北大学历史文化学院

**联系方式**: zzhjim@qq.com

**技术支持**: 华为云CodeArts Agent

**版本**: v1.2.0

**许可协议**: MIT License

## 功能特性

- 递归扫描文件夹中的所有PDF文件
- 提取PDF文件中的OCR文本层内容
- 保持原有的文件名和目录结构
- 支持文件名过滤(通配符匹配)
- **多线程并行处理**,大幅提升处理速度
- **智能跳过已处理文件**,避免重复工作
- **多种提取方法支持**: PYMUPDF、PDFPLUMBER、PyPDF2
- **智能方法选择**: 根据PDF特征自动选择最优提取方法
- **性能统计**: 实时监控各方法的处理性能
- **自动降级**: 失败时自动尝试其他方法
- 实时显示处理进度
- 详细的错误日志记录
- 图形化用户界面

## 系统要求

- Python 3.8 或更高版本
- Windows / Linux / macOS

## 安装

1. 克隆或下载本项目
2. 安装依赖:

```bash
pip install -r requirements.txt
```

## 使用方法

### 命令行运行

```bash
python main.py
```

### 使用步骤

1. 选择源文件夹(包含PDF文件的目录)
2. 选择输出文件夹(保存TXT文件的目录)
3. (可选)设置文件名过滤模式
4. (可选)勾选"启用多线程处理"并设置线程数(默认4个线程)
5. (可选)勾选"跳过已处理的文件"(默认勾选)
6. 点击"开始提取"按钮
7. 等待处理完成
8. 查看处理结果和错误日志

### 新功能说明

#### 多线程处理
- 启用多线程可以同时处理多个PDF文件,显著提升处理速度
- 建议根据CPU核心数设置线程数(通常为CPU核心数的1-2倍)
- 对于大量PDF文件,多线程处理效果更加明显

#### 跳过已处理文件
- 默认启用,自动跳过输出目录中已存在的TXT文件
- 避免重复处理,节省时间和资源
- 如需重新处理所有文件,请取消勾选此项或勾选"覆盖已存在的文件"

#### 提取方法选择 (v1.2.0新增)
- **自动选择(推荐)**: 根据PDF文件特征智能选择最优方法
  - 纯文本PDF优先使用PYMUPDF(速度最快)
  - 复杂布局PDF使用PDFPLUMBER(效果最好)
  - 扫描件PDF使用PDFPLUMBER
- **手动选择**: 可强制指定使用某种方法
  - PYMUPDF: 高性能提取,适合纯文本PDF和大文件
  - PDFPLUMBER: 擅长处理复杂布局和表格
  - PyPDF2: 纯Python实现,兼容性好

#### 性能统计 (v1.2.0新增)
- 实时记录各方法的处理次数、成功率、平均耗时
- 在"性能统计"标签页查看详细数据
- 帮助了解不同方法的性能表现

#### 自动降级 (v1.2.0新增)
- 当一种方法提取失败时,自动尝试其他方法
- 确保最大程度成功提取文本
- 可在配置中关闭此功能

### 打包为可执行文件

如果需要将程序打包为独立的可执行文件,可以使用PyInstaller:

```bash
# 安装PyInstaller
pip install pyinstaller

# 打包为单个可执行文件
pyinstaller --onefile --windowed pdf_ocr_extract.spec

# 或使用命令行直接打包
pyinstaller --onefile --windowed --name pdf_ocr_extract main.py
```

打包完成后,可执行文件位于 `dist/` 目录下:
- Windows: `dist/pdf_ocr_extract.exe`
- Linux/macOS: `dist/pdf_ocr_extract`

详细使用说明请参考 [用户手册](docs/user_guide.md)
故障排查请参考 [故障排查指南](docs/troubleshooting.md)

## 项目结构

```
pdf-ocr-extract/
├── src/
│   ├── core/           # 核心数据结构
│   ├── scanner/        # 文件扫描模块
│   ├── extractor/      # PDF文本提取模块
│   ├── writer/         # 文件写入模块
│   ├── coordinator/    # 任务协调层
│   └── gui/           # 图形界面
├── tests/              # 单元测试
├── docs/               # 文档
├── main.py            # 程序入口
├── requirements.txt   # 依赖列表
└── setup.py          # 安装配置
```

## 技术栈

- **GUI框架**: PyQt6
- **PDF处理**: PyMuPDF, pdfplumber, PyPDF2
- **编码检测**: chardet
- **开发语言**: Python 3.8+

## 许可证

MIT License
