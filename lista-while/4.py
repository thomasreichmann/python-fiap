## Exercício 4

# Elabore um programa que leia 5 números e informe a soma e a média desses números.

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

while True:
    num3 = input("Digite o terceiro número: ")
    if num3.isnumeric():
        num3 = int(num3)
        break
    print("Digite apenas números!")

while True:
    num4 = input("Digite o quarto número: ")
    if num4.isnumeric():
        num4 = int(num4)
        break
    print("Digite apenas números!")

while True:
    num5 = input("Digite o quinto número: ")
    if num5.isnumeric():
        num5 = int(num5)
        break
    print("Digite apenas números!")

soma = num1 + num2 + num3 + num4 + num5
media = soma / 5

print(f"Soma: {soma}")
print(f"Média: {media}")
