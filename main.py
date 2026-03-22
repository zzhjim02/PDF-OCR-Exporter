"""PDF OCR提取工具 - 主程序入口"""
import sys
from PyQt6.QtWidgets import QApplication
from PyQt6.QtCore import Qt

from src.gui import MainWindow


def main():
    """主函数"""
    # 创建应用程序实例
    app = QApplication(sys.argv)

    # 启用高DPI支持 (PyQt6不再需要手动设置,自动支持)
    # PyQt6默认已经启用高DPI支持,无需手动设置

    # 创建并显示主窗口
    window = MainWindow()
    window.show()

    # 启动事件循环
    sys.exit(app.exec())


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"程序启动失败: {e}")
        sys.exit(1)
