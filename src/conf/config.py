from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    DB_URL: str = "postgresql+asyncpg://postgres:567234@localhost:5432/contacts_app"

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"
        case_sensitive = True
        extra = "ignore"


settings = Settings()
