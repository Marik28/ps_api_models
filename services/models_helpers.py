def to_lower_camel_case(string: str) -> str:
    bits = []
    for index, bit in enumerate(string.split("_")):
        if index == 0:
            bits.append(bit)
        else:
            bits.append(bit.capitalize())
    return ''.join(bits)
