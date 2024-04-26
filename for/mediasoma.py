soma = 0

numerosPraPedir = 10
for i in range(numerosPraPedir):
    numero = input(f"Digite o {i + 1}o número: ")

    while not numero.isnumeric():
        print("Digite apenas números!")
        numero = input(f"Digite o {i + 1}o número: ")

    numero = int(numero)
    soma += numero

print(f"A soma dos números é {soma}.")
print(f"A média dos números é {soma / numerosPraPedir}")
