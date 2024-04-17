## Exercício 15

# Em uma eleição presidencial com quatro candidatos, os votos são informados por meio de códigos. Elabore um programa que
# calcule e mostre:
#
# - O total de votos para cada candidato;
# - O total de votos nulos;
# - O total de votos em branco;
# - A percentagem de votos nulos sobre o total de votos;
# - A percentagem de votos em branco sobre o total de votos.
#
# A entrada de dados termina com o valor zero.

votos_candidato_1 = votos_candidato_2 = votos_candidato_3 = votos_candidato_4 = votos_nulos = votos_brancos = 0

while True:
    voto = input("Digite o código do candidato ou 0 para sair: ")
    if voto.isnumeric():
        voto = int(voto)

        if voto == 0:
            break
        elif voto == 1:
            votos_candidato_1 += 1
        elif voto == 2:
            votos_candidato_2 += 1
        elif voto == 3:
            votos_candidato_3 += 1
        elif voto == 4:
            votos_candidato_4 += 1
        elif voto == 5:
            votos_nulos += 1
        elif voto == 6:
            votos_brancos += 1
    else:
        print("Digite apenas números!")

total_votos = votos_candidato_1 + votos_candidato_2 + votos_candidato_3 + votos_candidato_4 + votos_nulos + votos_brancos

percentual_nulos = (votos_nulos / total_votos) * 100
percentual_brancos = (votos_brancos / total_votos) * 100

print(f"Total de votos para o candidato 1: {votos_candidato_1}")
print(f"Total de votos para o candidato 2: {votos_candidato_2}")
print(f"Total de votos para o candidato 3: {votos_candidato_3}")
print(f"Total de votos para o candidato 4: {votos_candidato_4}")
print(f"Total de votos nulos: {votos_nulos}")
print(f"Total de votos em branco: {votos_brancos}")
print(f"Percentual de votos nulos sobre o total de votos: {percentual_nulos:.2f}%")
print(f"Percentual de votos em branco sobre o total de votos: {percentual_brancos:.2f}%")
