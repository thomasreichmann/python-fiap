numero = ""
numero_int = -1

while not numero.isnumeric() and numero_int < 0 or numero_int > 10:
    numero = input("Digite um número entre 0 e 10: ")
    if not numero.isnumeric():
        print("Digite apenas números!")
    else:
        numero_int = int(numero)
        if numero_int < 0 or numero_int > 10:
            print("O número deve estar entre 0 e 10!")

print("Número digitado: ", numero)
