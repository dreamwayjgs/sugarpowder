from sugarpowder.infixes import Infix, isa


def test_isa_int():
    assert (3 | isa | int) is True


def test_isa_str():
    assert ("hello" | isa | str) is True


def test_isa_wrong_type():
    assert (3 | isa | str) is False


def test_isa_subclass():
    assert (True | isa | int) is True  # bool is subclass of int


def test_custom_infix():
    contains = Infix(lambda a, b: a in b)
    assert (2 | contains | [1, 2, 3]) is True
    assert (5 | contains | [1, 2, 3]) is False
