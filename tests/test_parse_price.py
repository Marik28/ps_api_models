from services.parsing import parse_price


def test_parse_price_with_dot():
    text = "RUB 1.789"
    price, currency = parse_price(text)
    assert price == 1789
    assert currency == "RUB"


def test_parse_price_without_dot():
    text = "RUB 499"
    price, currency = parse_price(text)
    assert price == 499
    assert currency == "RUB"


def test_parse_price_with_incorrect_text():
    text = "7.898 RUB"
    price, currency = parse_price(text)
    assert price is None
    assert currency is None
