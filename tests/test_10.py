from main import ex10


def test_ex10_1():
    assert ex10(1, 1, 1) == "Equilátero"
    assert ex10(2, 2, 2) == "Equilátero"


def test_ex10_2():
    assert ex10(1, 2, 1) == "Isosceles"
    assert ex10(1, 1, 3) == "Isosceles"
    assert ex10(2, 2, 1) == "Isosceles"


def test_ex10_3():
    assert ex10(1, 2, 3) == "Escaleno"
    assert ex10(4, 2, 3) == "Escaleno"
    assert ex10(5, 4, 3) == "Escaleno"
