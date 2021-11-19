import datetime
import enum
import json
from pathlib import Path
from typing import Union, Optional

import requests
import typer

import models
from models import ApiResponse
from settings import settings

app = typer.Typer()


class PLATFORMS(enum.Enum):
    PS5_GAMES = "ps5_games"
    PS4_GAMES = "ps4_games"
    PS_VR_GAMES = "ps_vr_games"


query_ids = {
    PLATFORMS.PS5_GAMES.value: "4cbf39e2-5749-4970-ba81-93a489e4570c",
    PLATFORMS.PS4_GAMES.value: "44d8bb20-653e-431e-8ad0-c0a365f68d2f",
    PLATFORMS.PS_VR_GAMES.value: "95239ca7-2dcf-43d9-8d4b-b7672ee9304a",

}


def get_all_platform_games(platform_key: Union[str, PLATFORMS] = PLATFORMS.PS4_GAMES.value) -> list[models.Product]:
    if isinstance(platform_key, PLATFORMS):
        platform_key = platform_key.value

    platform_id = query_ids[platform_key]
    size = 1000
    offset = 0
    products = []
    while True:
        response = requests.get(
            f'https://web.np.playstation.com/api/graphql/v1//op?operationName=categoryGridRetrieve'
            f'&variables={{%22id%22:%22{platform_id}%22,%22pageArgs%22:{{%22size%22:{size},%22offset%22:{offset}}},%22sortBy%22:null,%22filterBy%22:[],%22facetOptions%22:[]}}'
            f'&extensions={{%22persistedQuery%22:{{%22version%22:1,%22sha256Hash%22:%224ce7d410a4db2c8b635a48c1dcec375906ff63b19dadd87e073f8fd0c0481d35%22}}}}',
            headers={
                "X-PSN-Store-Locale-Override": "ru-RU"
            })

        if response.status_code != 200:
            raise Exception(f"Ответ сервера плохой: {response.status_code}, {response.text}")

        api_response: ApiResponse = ApiResponse.parse_raw(response.text)
        products.extend(api_response.data.category_grid_retrieve.products)
        typer.echo(f"Получено {len(products)} из {api_response.data.category_grid_retrieve.page_info.total_count}")

        if api_response.data.category_grid_retrieve.page_info.is_last:
            break
        offset += size
    return products


def generate_filename(platform: PLATFORMS):
    return f"{platform.value}_{datetime.datetime.now().strftime('%d-%m-%Y_%H:%M:%S')}.json"


def save_products(products: list[models.Product], filename: str, directory: Optional[Path] = None):
    if directory is None:
        directory = settings.base_dir

    file_full_path = directory / filename
    with open(file_full_path, "w") as f:
        json.dump([product.dict() for product in products], f, indent=2, ensure_ascii=False)
    typer.echo(f"Данные сохранены в {file_full_path}")


@app.command()
def main(
        platform: PLATFORMS,
        output_directory: Optional[Path] = typer.Option(
            None,
            "--output_directory",
            "-o",
            resolve_path=True,
            exists=True,
        ),
        filename: Optional[str] = typer.Option(
            None,
            "--filename",
            "-f",
        ),
):
    if filename is None:
        filename = generate_filename(platform
                                     )
    products = get_all_platform_games(platform)
    save_products(products, filename, output_directory)


if __name__ == '__main__':
    app()
