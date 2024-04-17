## Exercício 7

# Crie um gerador de tabuada, capaz de gerar a tabuada de qualquer número inteiro entre 1 a 10. O usuário deve informar de
# qual número deseja ver a tabuada. A saída deve ser conforme o exemplo abaixo para a tabuada de 5:
#
# Tabuada de 5:
# 5 X 1 = 5
# 5 X 2 = 10
# ...
# 5 X 10 = 50

while True:
    num = input("Digite um número entre 1 e 10: ")
    if num.isnumeric():
        num = int(num)
        if 1 <= num <= 10:
            break
    print("Digite apenas números entre 1 e 10!")

print(f"Tabuada de {num}:")

i = 1
while i <= 10:
    print(f"{num} X {i} = {num * i}")
    i += 1
