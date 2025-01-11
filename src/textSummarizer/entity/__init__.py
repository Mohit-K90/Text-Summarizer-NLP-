# In textSummarizer/entity/__init__.py
from pathlib import Path

class DataIngestionConfig:
    def __init__(self, root_dir: Path, source_URL: str, local_data_file: Path, unzip_dir: Path):
        self.root_dir = root_dir
        self.source_URL = source_URL
        self.local_data_file = local_data_file
        self.unzip_dir = unzip_dir

class DataValidationConfig:
    def __init__(self, root_dir: Path, STATUS_FILE: str, ALL_REQUIRED_FILES: list):
        self.root_dir = root_dir
        self.STATUS_FILE = STATUS_FILE
        self.ALL_REQUIRED_FILES = ALL_REQUIRED_FILES
