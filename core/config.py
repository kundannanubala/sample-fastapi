from pydantic_settings import BaseSettings
import os
from pathlib import Path
from typing import ClassVar

class Settings(BaseSettings):
    ROOT_DIR: ClassVar[Path] = Path(__file__).parent.parent
    secret_key: str = os.environ.get("SECRET_KEY", "")
    LOGFIRE_TOKEN: str = os.environ.get("LOGFIRE_TOKEN", "")

    class Config:
        env_file = ".env"
        env_file_encoding = 'utf-8'
        case_sensitive = True
        extra = 'allow'

settings = Settings()

