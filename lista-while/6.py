## Exercício 6

# Desenvolva um programa que leia um nome de usuário e sua senha, não aceitando a senha igual ao nome do usuário. Mostre
# uma mensagem de erro e solicite as informações novamente.

nome = input("Digite seu nome de usuário: ")

while True:
    senha = input("Digite sua senha: ")

    if senha != nome:
        break

    print("Senha não pode ser igual ao nome de usuário!")

print("Usuário e senha cadastrados com sucesso!")
