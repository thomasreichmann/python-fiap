## Exercício 10

# Faça um programa que calcule o fatorial de um número inteiro fornecido pelo usuário. Por exemplo, 5! = 5.4.3.2.1 = 120.

while True:
    num = input("Digite um número inteiro: ")
    if num.isnumeric():
        num = int(num)
        break
    print("Digite apenas números!")

total = 1
while num > 0:
    total += total * (num - 1)
    num -= 1

print(total)
