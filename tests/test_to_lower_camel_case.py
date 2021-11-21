from services.models_helpers import to_lower_camel_case


def test_to_lower_camel_case_many_bits():
    text = "some_text_kekw"
    assert to_lower_camel_case(text) == "someTextKekw"


def test_to_lower_camel_case_one_bit():
    text = "word"
    assert to_lower_camel_case(text) == "word"
