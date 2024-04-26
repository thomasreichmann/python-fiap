par = 0
impar = 0

for i in range(10):
    numero = input(f"Digite o {i + 1}o número: ")

    while not numero.isnumeric():
        print("Digite apenas números!")
        numero = input(f"Digite o {i + 1}o número: ")

    numero = int(numero)
    if numero % 2 == 0:
        par += 1
    else:
        impar += 1

print(f"Foram digitados {par} números pares e {impar} números ímpares.")
