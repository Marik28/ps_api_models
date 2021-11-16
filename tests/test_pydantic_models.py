from models import ApiResponse


def test_json_parsing():
    """тест не должен упасть"""
    ApiResponse.parse_file("data/example_data.json")
