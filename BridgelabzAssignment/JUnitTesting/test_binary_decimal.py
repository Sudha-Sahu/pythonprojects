from JUnitTesting import binary_decimal_conv as bd


def test_no_negative_num():
    assert bd.decimal_to_binary(-16) == 1000

