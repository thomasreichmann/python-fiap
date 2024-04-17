import math


## Exercício 11

# Crie um programa que solicite um número inteiro e determine se ele é ou não um número primo.

def get_divisor(_num):
    if _num == 0:
        return None

    _start = 2
    _end = math.floor(math.sqrt(_num))

    prime = None
    _i = _start
    print(f"Verificando se o número {_num} é primo")
    print(
        f"Começando a verificar a partir de {_start} até {_end}, que elimina {((_num - _end) / _num * 100)}% dos números")
    while _i <= _end:
        if _num % _i == 0:
            prime = _i
            break

        if _i % 10000 == 0:
            print(f"Porcentagem de numeros verificados: {((_i - _start) / (_end - _start + 1) * 100):.2f}%")

        _i += 1

    return prime


for i in range(12031023123, 999999999929999999):
    divisor = get_divisor(i)

    if divisor:
        print(f"O número '{i}' não é primo! Ele é divisivel por '{divisor}'")
    else:
        print(f"O número '{i}' é primo!")
