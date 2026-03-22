"""核心模块"""
from .config import ExtractorConfig, ProcessingResult, PDFFileInfo, ExtractedText
from .exceptions import (
    PDFExtractorError,
    ConfigError,
    FileNotFoundError,
    PermissionError,
    PDFExtractionError,
    EncodingError,
    FileWriteError,
)

__all__ = [
    "ExtractorConfig",
    "ProcessingResult",
    "PDFFileInfo",
    "ExtractedText",
    "PDFExtractorError",
    "ConfigError",
    "FileNotFoundError",
    "PermissionError",
    "PDFExtractionError",
    "EncodingError",
    "FileWriteError",
]
