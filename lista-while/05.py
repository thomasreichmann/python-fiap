## Exercício 5

# Faça um programa que receba dois números inteiros e gere os números inteiros que estão no intervalo compreendido entre
# eles.

while True:
    while True:
        num1 = input("Digite o primeiro número: ")
        if num1.isnumeric():
            num1 = int(num1)
            break
        print("Digite apenas números!")

    while True:
        num2 = input("Digite o segundo número: ")
        if num2.isnumeric():
            num2 = int(num2)
            break
        print("Digite apenas números!")

    if num1 < num2:
        break

    print("O primeiro número deve ser menor que o segundo número!")

i = 1
while num1 + i < num2:
    print(num1 + i)
    i += 1
