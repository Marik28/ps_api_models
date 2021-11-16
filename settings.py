from pydantic import BaseSettings


class Settings(BaseSettings):
    database_url: str = "sqlite:///db.sqlite3"


settings = Settings()
