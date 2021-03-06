import sqlalchemy.orm
import typer
from sqlalchemy.exc import IntegrityError

import models
import tables
from services.parsing import parse_price, parse_discount
from services.platforms import get_platform_by_name


def insert_products(session: sqlalchemy.orm.Session, products: list[models.Product]):
    products_to_create = [parse_product(session, product) for product in products
                          if not is_free(product)]
    with typer.progressbar(
            products_to_create,
            fill_char="█",
            empty_char=" ",
            bar_template="%(label)s  %(bar)s  %(info)s",
    ) as progress:
        for product in progress:
            session.add(product)
            try:
                session.commit()
            except IntegrityError:
                session.rollback()


def parse_product(session: sqlalchemy.orm.Session, product: models.Product) -> tables.Product:
    platforms = [get_platform_by_name(session, platform.value) for platform in product.platforms]

    classification = product.localized_store_display_classification.value

    assert product.price is not None, "Должна присутствовать цена"
    assert len(product.skus) > 0, "Обычно тут только одно значение лежит"
    is_preorder = product.skus[0].type == models.SkuType.PREORDER

    base_price_in_rubles, _ = parse_price(product.price.base_price)
    base_price_in_rubles = 0 if base_price_in_rubles is None else base_price_in_rubles

    discounted_price_in_rubles, _ = parse_price(product.price.discounted_price)
    discounted_price_in_rubles = 0 if discounted_price_in_rubles is None else discounted_price_in_rubles

    discount_percentage = parse_discount(product.price.discount_text)
    discount_percentage = 0 if discount_percentage is None else discount_percentage

    logo_urls = [media.url for media in product.media if media.role == models.MediaRole.LOGO]

    if not logo_urls:
        logo_url = None
    else:
        logo_url = logo_urls[0]

    return tables.Product(
        id=product.id,
        name=product.name,
        np_title_id=product.np_title_id,
        classification=classification,
        logo_url=logo_url,
        is_preorder=is_preorder,
        base_price_in_rubles=base_price_in_rubles,
        discounted_price_in_rubles=discounted_price_in_rubles,
        discount_percentage=discount_percentage,
        platforms=platforms,
    )


def is_free(product: models.Product) -> bool:
    return product.price is None or product.price.is_free or product.price.base_price == "Недоступно"
