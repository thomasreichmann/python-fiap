lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

par = []
impar = []

for numero in lista:
    if numero % 2 == 0:
        par.append(numero)
    else:
        impar.append(numero)

print(f"Números pares: {par}")
print(f"Números ímpares: {impar}")
