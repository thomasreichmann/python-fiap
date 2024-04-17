from main import ex8


def test_triangulo_correct_perimeter():
    tam = 1
    lados = 3
    res = ex8(lados, tam)
    assert res == "TRIÂNGULO" + str(tam * lados)


def test_quadrado_correct_perimeter():
    tam = 1
    lados = 4
    res = ex8(lados, tam)
    assert res == "QUADRADO" + str(tam * lados)


def test_pentagono_without_perimeter():
    tam = 1
    lados = 5
    res = ex8(lados, tam)
    assert res == "PENTÁGONO"


# Caso o número de lados seja inferior a 3 escrever NÃO É UM POLÍGONO.
# Caso o número de lados seja superior a 5 escrever POLÍGONO NÃO IDENTIFICADO.

def test_hexagono_not_identified():
    tam = 1
    lados = 6
    res = ex8(lados, tam)
    assert res == "POLÍGONO NÃO IDENTIFICADO"


def test_not_a_poligono():
    tam = 1
    lados = 2
    res = ex8(lados, tam)
    assert res == "NÃO É UM POLÍGONO"
