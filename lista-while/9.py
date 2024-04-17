## Exercício 9

# Elabore um programa que solicite 10 números inteiros, calcule e mostre a quantidade de números pares e ímpares.

print("Digite 10 números inteiros:")

pares = 0
impares = 0

i = 0
while i < 10:
    while True:
        numero = input(f"Digite o {i + 1}º número: ")
        if numero.isnumeric():
            numero = int(numero)
            break
        print("Digite apenas números!")

    if numero % 2 == 0:
        pares += 1
    else:
        impares += 1

    i += 1

print(f"Quantidade de números pares: {pares}")
print(f"Quantidade de números ímpares: {impares}")
