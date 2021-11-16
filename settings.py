from pathlib import Path

from pydantic import BaseSettings


class Settings(BaseSettings):
    base_dir: Path = Path(__file__).resolve().parent
    database_url: str = f"sqlite:///{base_dir / 'db.sqlite3'}"


settings = Settings()
