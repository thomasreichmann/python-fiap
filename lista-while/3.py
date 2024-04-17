## Exercício 3

# Considerando que a população do país A seja de 80.000 habitantes com uma taxa anual de crescimento de 3%, e a população
# do país B seja de 200.000 habitantes com uma taxa de crescimento de 1.5%, desenvolva um programa que calcule e exiba o
# número de anos necessários para que a população do país A ultrapasse ou iguale a população do país B, mantendo as taxas
# de crescimento.

populacao_a = 80000
populacao_b = 200000

anos = 0

while True:
    anos += 1
    populacao_a *= 1.03
    populacao_b *= 1.015

    if populacao_a >= populacao_b:
        break

print(f"Serão necessários {anos} anos para a população do país A ultrapassar a população do país B.")
