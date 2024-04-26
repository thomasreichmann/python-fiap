import math

## Exercício 11

# Crie um programa que solicite um número inteiro e determine se ele é ou não um número primo.

while True:
    num = input("Digite um número inteiro: ")
    if num.isnumeric():
        num = int(num)
        break
    print("Digite apenas números!")

end = math.floor(math.sqrt(num))
start = 2
print(f"Começando a verificar a partir de {start} até {end}, que elimina {((num - end) / num * 100)}% dos números")
if num > 2:
    curr = start
    while True:
        if num % curr == 0:
            print(f"O número '{num}' não é primo! Ele é divisivel por '{curr}'")
            print(f"{num} / {curr} = {int(num / curr)}")
            break

        if curr % 10000 == 0:
            print(f"Porcentagem de numeros verificados: {((curr - start) / (end - start + 1) * 100):.2f}%")

        if curr == end:
            print(f"O número '{num}' é primo!")
            break

        curr += 1
elif num == 0:
    print(f"0 não é primo!")
else:
    print(f"O número '{num}' é primo!")
