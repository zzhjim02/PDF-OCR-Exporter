# PDF OCR Text Extraction Master / PDF OCR文本提取大师

A professional PDF OCR text extraction tool that supports batch processing, multi-threading, and intelligent skipping.
一个专业的PDF OCR文本提取工具，支持批量处理、多线程并行、智能跳过等功能。

## Copyright Information / 版权信息

*   **Author / 作者**: 浮生＆2cm
*   **Affiliation / 单位**: School of History and Culture, Hubei University / 湖北大学历史文化学院
*   **Contact / 联系方式**: zzhjim@qq.com
*   **Technical Support / 技术支持**: Huawei Cloud CodeArts Agent / 华为云CodeArts Agent
*   **Version / 版本**: v1.2.0
*   **License / 许可协议**: MIT License

## Feature Highlights / 功能特性

*   **Recursive Folder Scanning / 递归扫描文件夹**: Scans all PDF files in the specified folder and its subfolders. / 扫描文件夹中的所有PDF文件，包括子文件夹。
*   **OCR Text Layer Extraction / 提取OCR文本层**: Extracts text from the OCR layer of PDF files. / 提取PDF文件中的OCR文本层内容。
*   **Original Structure Preservation / 保持原有结构**: Maintains the original filenames and directory structure. / 保持原有的文件名和目录结构。
*   **Filename Filtering / 文件名过滤**: Supports filename filtering using wildcard patterns. / 支持文件名过滤（通配符匹配）。
*   **Multi-threaded Parallel Processing / 多线程并行处理**: Significantly speeds up processing by handling multiple PDFs simultaneously. / 大幅提升处理速度。
*   **Smart Skip of Processed Files / 智能跳过已处理文件**: Automatically skips files that have already been processed to avoid redundant work. / 避免重复工作，节省时间。
*   **Multiple Extraction Methods / 多种提取方法支持**: Supports PYMUPDF, PDFPLUMBER, and PyPDF2. / 支持PYMUPDF、PDFPLUMBER、PyPDF2。
*   **Intelligent Method Selection / 智能方法选择**: Automatically selects the optimal extraction method based on PDF characteristics. / 根据PDF特征自动选择最优提取方法。
*   **Performance Statistics / 性能统计**: Monitors and displays real-time performance data for each extraction method. / 实时监控各方法的处理性能。
*   **Automatic Degradation / 自动降级**: Automatically tries alternative methods if one extraction attempt fails. / 失败时自动尝试其他方法。
*   **Real-time Progress Display / 实时显示处理进度**: Shows the current processing progress clearly. / 实时显示处理进度。
*   **Detailed Error Logging / 详细的错误日志记录**: Records errors for troubleshooting and reference. / 详细的错误日志记录。
*   **Graphical User Interface (GUI) / 图形化用户界面**: Easy-to-use interface built with PyQt6. / 图形化用户界面。

## System Requirements / 系统要求

*   **Python**: 3.8 or higher / 3.8 或更高版本
*   **Operating System / 操作系统**: Windows / Linux / macOS

## Installation / 安装

1.  Clone or download this project. / 克隆或下载本项目。
2.  Install dependencies: / 安装依赖：

```bash
pip install -r requirements.txt
```

## Usage Instructions / 使用方法

### Run via Command Line / 命令行运行

```bash
python main.py
```

### Step-by-Step Guide / 使用步骤

1.  **Select Source Folder / 选择源文件夹**: Choose the directory containing your PDF files. / 选择包含PDF文件的目录。
2.  **Select Output Folder / 选择输出文件夹**: Choose the directory where you want to save the extracted TXT files. / 选择保存TXT文件的目录。
3.  **(Optional) Set Filename Filter / (可选)设置文件名过滤模式**: Use wildcard patterns to filter which PDFs to process. / 设置文件名过滤模式。
4.  **(Optional) Enable Multi-threading / (可选)启用多线程处理**: Check the box and set the number of threads (default: 4). / 勾选并设置线程数（默认4个线程）。
5.  **(Optional) Skip Processed Files / (可选)跳过已处理的文件**: This is enabled by default to avoid reprocessing. / 默认勾选，避免重复处理。
6.  **Start Extraction / 点击"开始提取"按钮**: Click the "Start Extraction" button. / 点击"开始提取"按钮。
7.  **Wait for Completion / 等待处理完成**: The progress bar will show the status. / 等待处理完成。
8.  **View Results / 查看处理结果**: Check the output folder for TXT files and review error logs if needed. / 查看处理结果和错误日志。

### New Feature Details / 新功能说明

#### Multi-threaded Processing / 多线程处理

*   Enabling multi-threading allows simultaneous processing of multiple PDF files, drastically reducing total processing time. / 启用多线程可以同时处理多个PDF文件，显著提升处理速度。
*   It is recommended to set the number of threads to 1-2 times the number of CPU cores for optimal performance. / 建议根据CPU核心数设置线程数（通常为CPU核心数的1-2倍）。
*   Especially effective when dealing with large batches of PDF files. / 对于大量PDF文件，多线程处理效果更加明显。

#### Skip Processed Files / 跳过已处理文件

*   Enabled by default, this feature automatically skips any TXT files that already exist in the output directory. / 默认启用，自动跳过输出目录中已存在的TXT文件。
*   Saves time and computational resources by avoiding redundant work. / 避免重复处理，节省时间和资源。
*   To reprocess all files, uncheck this option or enable "Overwrite Existing Files." / 如需重新处理所有文件，请取消勾选此项或勾选"覆盖已存在的文件"。

#### Extraction Method Selection (New in v1.2.0) / 提取方法选择 (v1.2.0新增)

*   **Auto Select (Recommended) / 自动选择(推荐)**: Intelligently chooses the best method based on PDF features. / 根据PDF文件特征智能选择最优方法。
    *   Plain text PDFs prioritize PYMUPDF (fastest speed). / 纯文本PDF优先使用PYMUPDF（速度最快）。
    *   Complex layout PDFs use PDFPLUMBER (best results). / 复杂布局PDF使用PDFPLUMBER（效果最好）。
    *   Scanned PDFs use PDFPLUMBER. / 扫描件PDF使用PDFPLUMBER。
*   **Manual Select / 手动选择**: Force the use of a specific method. / 可强制指定使用某种方法。
    *   **PYMUPDF**: High-performance extraction, ideal for large files and plain text. / 高性能提取，适合纯文本PDF和大文件。
    *   **PDFPLUMBER**: Excellent for tables and complex layouts. / 擅长处理复杂布局和表格。
    *   **PyPDF2**: Pure Python implementation with good cross-version compatibility. / 纯Python实现，兼容性好。

#### Performance Statistics (New in v1.2.0) / 性能统计 (v1.2.0新增)

*   Tracks real-time metrics including processing count, success rate, and average time per method. / 实时记录各方法的处理次数、成功率、平均耗时。
*   View detailed data in the "Performance Statistics" tab. / 在"性能统计"标签页查看详细数据。
*   Helps users understand the efficiency of different extraction methods. / 帮助了解不同方法的性能表现。

#### Automatic Degradation (New in v1.2.0) / 自动降级 (v1.2.0新增)

*   If one extraction method fails, the tool automatically switches to another method to ensure maximum success rate. / 当一种方法提取失败时，自动尝试其他方法。
*   Ensures the highest possible text extraction success rate. / 确保最大程度成功提取文本。
*   This feature can be disabled in the settings if needed. / 可在配置中关闭此功能。

### Packaging into Executable File / 打包为可执行文件

To package the program into a standalone executable, use PyInstaller: / 如果需要将程序打包为独立的可执行文件，可以使用PyInstaller：

```bash
# Install PyInstaller / 安装PyInstaller
pip install pyinstaller

# Package into a single executable file / 打包为单个可执行文件
pyinstaller --onefile --windowed pdf_ocr_extract.spec

# Or directly package using the command line / 或使用命令行直接打包
pyinstaller --onefile --windowed --name pdf_ocr_extract main.py
```

After packaging, the executable will be located in the `dist/` directory: / 打包完成后，可执行文件位于 `dist/` 目录下：

*   **Windows**: `dist/pdf_ocr_extract.exe`
*   **Linux/macOS**: `dist/pdf_ocr_extract`

For detailed usage instructions, please refer to the [User Manual](docs/user_guide.md). / 详细使用说明请参考 [用户手册](docs/user_guide.md)。
For troubleshooting, refer to the [Troubleshooting Guide](docs/troubleshooting.md). / 故障排查请参考 [故障排查指南](docs/troubleshooting.md)。

## Project Structure / 项目结构

```
pdf-ocr-extract/
├── src/
│   ├── core/           # Core data structures / 核心数据结构
│   ├── scanner/        # File scanning module / 文件扫描模块
│   ├── extractor/      # PDF text extraction module / PDF文本提取模块
│   ├── writer/         # File writing module / 文件写入模块
│   ├── coordinator/    # Task coordination layer / 任务协调层
│   └── gui/           # Graphical interface / 图形界面
├── tests/              # Unit tests / 单元测试
├── docs/               # Documentation / 文档
├── main.py            # Program entry point / 程序入口
├── requirements.txt   # Dependency list / 依赖列表
└── setup.py          # Installation configuration / 安装配置
```

## Technical Stack / 技术栈

*   **GUI Framework / GUI框架**: PyQt6
*   **PDF Processing / PDF处理**: PyMuPDF, pdfplumber, PyPDF2
*   **Encoding Detection / 编码检测**: chardet
*   **Programming Language / 开发语言**: Python 3.8+

## License / 许可证

MIT License
