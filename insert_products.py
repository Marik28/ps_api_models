import json
from pathlib import Path

import typer

import models
from add_data_to_db import insert_products
from database import Session

app = typer.Typer()


@app.command()
def main(
        json_file: Path = typer.Argument(
            ...,
            resolve_path=True,
            exists=True,
            readable=True,
        )
):
    with open(json_file) as f:
        products = json.load(f)

    products_to_create = []
    for product in products:
        product_to_create = models.Product.parse_obj(product)
        products_to_create.append(product_to_create)
    with Session() as session:
        insert_products(session, products_to_create)


if __name__ == '__main__':
    app()
