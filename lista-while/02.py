# Crie um programa que leia e valide as seguintes informações:
# - **Estado Civil:** deve ser 's', 'c', 'v', 'd'.

while True:
    nome = input("Digite seu nome: ")
    if len(nome) > 3:
        break
    print("Nome deve ter mais de 3 caracteres!")

while True:
    idade = input("Digite sua idade: ")
    if idade.isnumeric():
        idade = int(idade)
        if 0 <= idade <= 150:
            break
    print("Idade deve estar entre 0 e 150!")

while True:
    salario = input("Digite seu salário: ")
    if salario.isnumeric():
        salario = float(salario)
        if salario > 0:
            break
    print("Salário deve ser maior que zero!")

while True:
    sexo = input("Digite seu sexo (f/m): ")
    if sexo in ['f', 'm']:
        break
    print("Sexo deve ser 'f' ou 'm'!")

while True:
    estado_civil = input("Digite seu estado civil (s/c/v/d): ")
    if estado_civil == 's' or estado_civil == "c" or estado_civil == "v" or estado_civil == "d":
        break
    print("Estado civil deve ser 's', 'c', 'v' ou 'd'!")

print("Nome: ", nome)
print("Idade: ", idade)
print("Salário: ", salario)
print("Sexo: ", sexo)
print("Estado civil: ", estado_civil)
