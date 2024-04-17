## Exercício 14

# Faça um programa que leia uma quantidade indeterminada de números positivos e conte quantos deles estão nos seguintes
# intervalos: [0-25], [26-50], [51-75] e [76-100]. O programa termina quando um número negativo é lido.

qtd_0_25 = qtd_26_50 = qtd_51_75 = qtd_76_100 = 0

while True:
    num = input("Digite um número positivo: ")
    if num.isnumeric():
        num = int(num)

        if num <= 25:
            qtd_0_25 += 1
        elif num <= 50:
            qtd_26_50 += 1
        elif num <= 75:
            qtd_51_75 += 1
        elif num <= 100:
            qtd_76_100 += 1
    else:
        break

print(f"Quantidade de números no intervalo [0-25]: {qtd_0_25}")
print(f"Quantidade de números no intervalo [26-50]: {qtd_26_50}")
print(f"Quantidade de números no intervalo [51-75]: {qtd_51_75}")
print(f"Quantidade de números no intervalo [76-100]: {qtd_76_100}")
