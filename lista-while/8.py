## Exercício 8

# Desenvolva um programa capaz de gerar a série de Fibonacci até o n-ésimo termo.

while True:
    n = input("Digite o n-ésimo termo da série de Fibonacci: ")
    if n.isnumeric():
        n = int(n)

        if n > 3:
            break
    print("Digite apenas números maiores de 3!")

print(f"Calculando o a serie de Fibonacci ate o {n}-esimo termo")

termo1 = 1
termo2 = 1
termo3 = 2

print(termo1)
print(termo2)
print(termo3)

i = 4
while i < n:
    _2 = termo2
    _3 = termo3

    termo3 = termo2 + termo3
    termo2 = _3
    termo1 = _2

    i += 1

    print(str(termo3) + " " + str(i))
