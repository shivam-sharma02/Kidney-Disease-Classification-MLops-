from dataclasses import dataclass
from pathlib import Path

#this dataclass decorator used to avoid boilerplate code and this is defined
#so one can use its variable or attributes, it will return it as entity
#frozen - true makes it immutable -> if any request to change -> then throws error

@dataclass(frozen=True)
class DataIngestionConfig:
    root_dir: Path
    source_URL: str
    local_data_file: Path
    unzip_dir: Path