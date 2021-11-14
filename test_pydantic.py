from pprint import pprint

from models import ApiResponse

if __name__ == '__main__':
    r = ApiResponse.parse_file("data/example_data.json")
    products = r.data.category_grid_retrieve.products
    pprint(products)
