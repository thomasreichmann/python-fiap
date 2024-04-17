## Exercício 12

# Desenvolva um programa que calcule e mostre a média aritmética de N notas.

while True:
    n = input("Digite a quantidade de notas: ")
    if n.isnumeric():
        n = int(n)
        break
    print("Digite apenas números!")

i = 0
soma = 0
while i < n:
    while True:
        nota = input(f"Digite a {i + 1}ª nota: ")
        if nota.isnumeric():
            nota = int(nota)
            break
        print("Digite apenas números!")

    soma += nota
    i += 1

media = soma / n
print(f"Média aritmética das notas: {media}")
