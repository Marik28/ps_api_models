from typer.testing import CliRunner

from database import Session, engine
from scripts.insert_products import app
from services.platforms import insert_platforms
from settings import settings
from tables import Base


# todo добавить отдельную бд для тестов

def test_insert_products():
    runner = CliRunner()
    """Тест не должен падать"""
    Base.metadata.create_all(engine)
    with Session() as session:
        try:
            insert_platforms(session)
        except Exception as e:
            print("ошибка", e)
        runner.invoke(app, [str(settings.base_dir / "data/test_data.json")])
