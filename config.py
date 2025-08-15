from pydantic_settings import BaseSettings, SettingsConfigDict
from enum import Enum
from typing import Self
from pydantic import EmailStr, FilePath, HttpUrl, DirectoryPath, BaseModel


class Browser(str, Enum):
    WEBKIT = 'webkit'
    FIREFOX = 'firefox'
    CHROMIUM = 'chromium'

class TestUser(BaseModel):
    email: EmailStr
    username: str
    password: str

class TestData(BaseModel):
    image_png_file: FilePath

class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        env_nested_delimiter="."
    )
    app_url: HttpUrl
    headless: bool
    browser: list[Browser]
    test_user: TestUser
    test_data: TestData
    videos_dir: DirectoryPath
    tracing_dir: DirectoryPath
    storage_state_file: FilePath

    @classmethod
    def initialize(cls) -> Self:
        videos_dir = DirectoryPath("./videos")
        tracing_dir = DirectoryPath("./tracing")
        storage_state_file = FilePath("storage-state")

        videos_dir.mkdir(exist_ok=True)
        tracing_dir.mkdir(exist_ok=True)
        storage_state_file.touch(exist_ok=True)

        return Settings(
            videos_dir=videos_dir,
            tracing_dir=tracing_dir,
            storage_state_file=storage_state_file
        )

    def get_base_url(self) -> str:
        return f"{self.app_url}/"

settings = Settings.initialize()