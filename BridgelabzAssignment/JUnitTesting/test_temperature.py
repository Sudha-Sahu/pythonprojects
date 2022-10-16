from JUnitTesting import temperature_conversion as tc


def test_temp_conversion():
    assert tc.convert_temperature("abc") == "error"


def test_temp_positive():
    assert tc.convert_temperature(+56) == 2
