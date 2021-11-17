import models
from add_data_to_db import insert_platforms, insert_products
from database import Session, engine
from settings import settings
from tables import Base


# todo добавить отдельную бд для тестов

def test_insert_products():
    """Тест не должен падать"""
    Base.metadata.create_all(engine)
    with Session() as session:
        try:
            insert_platforms(session)
        except Exception as e:
            print("ошибка", e)
        r = models.ApiResponse.parse_file(settings.base_dir / "data/example_data.json")
        products = r.data.category_grid_retrieve.products
        insert_products(session, products)
