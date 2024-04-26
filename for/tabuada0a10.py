# Faça a tabuada de todos os numeros de 1 a 10 usando for

for i in range(1, 11):
    print(f"Tabuada de {i}:")
    for j in range(1, 11):
        print(f"{i} X {j} = {i * j}")
    print()
