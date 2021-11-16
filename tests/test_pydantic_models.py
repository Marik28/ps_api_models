from models import ApiResponse
from settings import settings


def test_json_parsing():
    """тест не должен упасть"""
    ApiResponse.parse_file(settings.base_dir / "data/example_data.json")
