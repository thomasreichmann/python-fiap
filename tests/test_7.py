from main import ex7


def test_triangulo_correct_perimeter():
    res = ex7(3, 1, 2, 3, None)
    assert res == "TRIÂNGULO" + str(1 + 2 + 3)


def test_quadrado_correct_perimeter():
    res = ex7(4, 1, 2, 3, 4)
    assert res == "QUADRADO" + str(1 + 2 + 3 + 4)


def test_pentagono_without_perimeter():
    res = ex7(5, 1, 2, 3, 4)
    assert res == "PENTÁGONO"

