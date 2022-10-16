from JUnitTesting import vending_machine as vm


def test_vending_machine():
    assert vm.get_change(1000) == "1000 X 1"

