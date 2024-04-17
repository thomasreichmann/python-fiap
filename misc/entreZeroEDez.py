while True:
    numero = input("Digite um número entre 0 e 10: ")

    if not numero.isnumeric():
        print("Digite apenas números!")
    else:
        numero = int(numero)
        if numero < 0 or numero > 10:
            print("O número deve estar entre 0 e 10!")
        else:
            break

print("Número digitado: ", numero)
