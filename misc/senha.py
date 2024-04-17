senha_u = input("Digite sua senha: ")
senha = "1234"

tentativas = 1
while senha_u != senha and tentativas < 5:
    senha_u = input("Senha incorreta! Tente novamente: ")
    tentativas += 1

if tentativas >= 5:
    print("Limite de tentativas excedido!")
else:
    print("Senha correta!")
