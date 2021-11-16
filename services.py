import re
from typing import Optional

import sqlalchemy.orm

import tables


def parse_price(text: str) -> tuple[Optional[int], Optional[str]]:
    """
    (text) -> (price, currency)
    """
    price_pattern = re.compile(r"^(?P<currency>\w+)\s+(?P<price>[\d.]*)$")
    result = price_pattern.match(text)

    if result is not None:
        price = int(result.group("price").replace(".", ""))
        currency = result.group("currency")
        return price, currency

    return None, None


def parse_discount(text: Optional[str]) -> int:
    if text is None:
        return 0
    return int(text[1:-1])


def get_platform_by_name(session: sqlalchemy.orm.Session, name: str) -> Optional[tables.Platform]:
    return session.query(tables.Platform).filter(tables.Platform.name == name).first()
