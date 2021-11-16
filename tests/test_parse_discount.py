from services import parse_discount


def test_parse_discount():
    text = "-15%"
    discount = parse_discount(text)
    assert discount == 15
