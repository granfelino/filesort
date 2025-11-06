"""
Constants module.

This module contains constants used in the project which hold file extensions
of most often used files (image, docs, spreadsheets, audio, code, etc.). They
are imported in the source code as well as in tests.
"""

# Image file extensions
IMAGE_EXTENSIONS = [
    ".jpg", ".jpeg", ".png", ".gif", ".bmp", ".tiff", ".svg", ".webp", ".heic"
]

# Document file extensions
DOCUMENT_EXTENSIONS = [
    ".txt", ".pdf", ".doc", ".docx", ".odt", ".rtf", ".tex", ".md"
]

# Spreadsheet file extensions
SPREADSHEET_EXTENSIONS = [
    ".xls", ".xlsx", ".ods", ".csv", ".tsv"
]

# Presentation file extensions
PRESENTATION_EXTENSIONS = [
    ".ppt", ".pptx", ".odp"
]

# Audio file extensions
AUDIO_EXTENSIONS = [
    ".mp3", ".wav", ".aac", ".flac", ".ogg", ".wma", ".m4a"
]

# Video file extensions
VIDEO_EXTENSIONS = [
    ".mp4", ".mkv", ".avi", ".mov", ".wmv", ".flv", ".webm"
]

# Archive / compressed file extensions
ARCHIVE_EXTENSIONS = [
    ".zip", ".rar", ".tar", ".gz", ".7z", ".bz2", ".xz"
]

# Code / script file extensions
CODE_EXTENSIONS = [
    ".py", ".js", ".ts", ".java", ".c", ".cpp", ".cs", ".rb", ".php",
    ".html", ".css", ".json", ".xml", ".sh", ".bat"
]

# Font file extensions
FONT_EXTENSIONS = [
    ".ttf", ".otf", ".woff", ".woff2"
]

# Misc / other common file extensions
MISC_EXTENSIONS = [
    ".log", ".cfg", ".ini", ".env", ".bak", ".tmp"
]

ALL_EXTENSION_LISTS = [
    IMAGE_EXTENSIONS,
    DOCUMENT_EXTENSIONS,
    SPREADSHEET_EXTENSIONS,
    PRESENTATION_EXTENSIONS,
    AUDIO_EXTENSIONS,
    VIDEO_EXTENSIONS,
    ARCHIVE_EXTENSIONS,
    CODE_EXTENSIONS,
    FONT_EXTENSIONS,
    MISC_EXTENSIONS
]

ALL_EXTENSION_TYPES = [
    "image",
    "document",
    "spreadsheet",
    "presentation",
    "audio",
    "video",
    "archive",
    "code",
    "font",
    "misc"
]

ALL_EXTENSIONS_SETS = {k : set(v) for k, v in zip(ALL_EXTENSION_TYPES, ALL_EXTENSION_LISTS)}

TEST_FILE_NAME = "file"
