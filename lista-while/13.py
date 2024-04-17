## Exercício 13

# Um funcionário recebe aumento salarial anualmente. Sabendo que:
#
# 1. Foi contratado em 1995, com salário inicial de R$ 1.000,00;
# 2. Em 1996 recebeu aumento de 1,5% sobre seu salário inicial;
# 3. A partir de 1997, os aumentos salariais sempre correspondem ao dobro do percentual do ano anterior;
#
# Crie um programa que determine o salário atual desse funcionário. Em seguida, modifique o programa permitindo que o
# usuário informe o salário inicial do funcionário.

while True:
    salario = input("Digite o salário inicial do funcionário: ")
    if salario.isnumeric():
        salario = float(salario)
        break
    print("Digite apenas números!")

ano = 1995
percentual = 1.5
salario_atual = salario
while ano < 2024:
    salario_atual += salario_atual * (percentual / 100)
    percentual *= 2
    ano += 1

print(f"Salário atual do funcionário em 2024: R$ {salario_atual:.2f}")
