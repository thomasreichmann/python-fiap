# Retorna o maior valor de 2
def ex1(val1, val2):
    # Escreva um programa para ler 2 valores
    # (considere que não serão informados valores iguais) e escrever o maior deles.
    if val1 > val2:
        return val1
    else:
        return val2


# Retorna true/false se pode votar esse ano
def ex2(ano_de_nascimento):
    # Escreva um programa para ler o ano de nascimento de uma pessoa e escrever uma mensagem que diga se ela poderá ou
    # não votar este ano (não é necessário considerar o mês em que ela nasceu).

    # Melhor buscar a data atual ao invés de usar o numero magico "2024"
    idade = 2024 - ano_de_nascimento

    return idade > 15


# Returns true if the password is correct (1234)
def ex3(senha):
    # Escreva um programa que verifique a validade de uma senha fornecida pelo usuário.
    # A senha válida é o número 1234. Devem ser impressas as seguintes mensagens:
    #
    # ACESSO PERMITIDO caso a senha seja válida.
    # ACESSO NEGADO caso a senha seja inválida.

    return senha == '1234'


# Calculates total purchase value, normal unit price is 0.30, if at least 12 its 0.25
def ex4(quant):
    # As maçãs custam R$ 0,30 cada se forem compradas menos do que uma dúzia,
    # e R$ 0,25 se forem compradas pelo menos doze.
    # Escreva um programa que leia o número de maçãs compradas, calcule e escreva o valor total da compra.

    price = 0.30
    if quant >= 12:
        price = 0.25

    return quant * price


# Should return in correct crescent order the string of values
# desnecessário, ex5_2() resolve de maneira mais elegante com apenas 3 comparações
def ex5(val1, val2, val3):
    # Escreva um programa para ler 3 valores inteiros
    # (considere que não serão lidos valores iguais) e escrevê-los em ordem crescente.

    a = val1
    b = val2
    c = val3

    if a > b:
        aux = b
        b = a
        a = aux
        # agora sei que a é menor que b

    if b > c:
        aux = c
        c = b
        b = aux

    if a > b:
        aux = b
        b = a
        a = aux
        # agora sei que a é menor que b

    if a > c:
        aux = c
        c = a
        a = aux
        # agora eu sei que a é o menor número

    return str(a) + str(b) + str(c)


def ex5_2(val1, val2, val3):
    # Escreva um programa para ler 3 valores inteiros
    # (considere que não serão lidos valores iguais) e escrevê-los em ordem crescente.

    a = val1
    b = val2
    c = val3

    '''
    Algorítimo usado
    
    Se o A for menor maior que o B, troca
    logo A é menor que o B
    Se o C for menor que o A, troca
    logo A é o menor dos três
    
    Se B for maior que o C, troca
    logo, a,b,c estão ordenados
    '''
    if a > b:
        aux = a
        a = b
        b = aux

    if c < a:
        aux = a
        a = c
        c = aux

    if b > c:
        aux = b
        b = c
        c = aux

    return str(a) + str(b) + str(c)


# Give height and sex (feminino, masculino) print the ideal weight using (72.7 * Altura) - 58 | (62.1 * Altura) — 44.7
def ex6(altura, sexo):
    # Tendo como entrada a altura e o sexo (codificado da seguinte forma: 1:feminino 2:masculino) de uma pessoa,
    # construa um programa que calcule e imprima seu peso ideal, utilizando as seguintes Fórmulas:
    # para homens: (72.7 * Altura) - 58
    # para mulheres: (62.1 * Altura) — 44.7

    if sexo == "feminino":
        return (72.7 * altura) - 58
    elif sexo == "masculino":
        return (62.1 * altura) - 44.7

    return False


def ex7(lados, len1, len2, len3, len4):
    # Escreva um programa para ler o número de lados de um polígono regular e a medida do lado (em cm). Calcular e imprimir o seguinte:
    #
    # Se o número de lados for igual a 3 escrever TRIÂNGULO e o valor do seu perímetro.
    # Se o número de lados for igual a 4 escrever QUADRADO e o valor da sua perímetro.
    # Se o número de lados for igual a 5 escrever PENTÁGONO.

    forma = ""
    per = ""

    if lados == 3:
        forma = "TRIÂNGULO"
        per = len1 + len2 + len3
    elif lados == 4:
        forma = "QUADRADO"
        per = len1 + len2 + len3 + len4
    else:
        forma = "PENTÁGONO"

    return forma + str(per)


def ex8(lados, tamanho):
    # Acrescente as seguintes mensagens à solução do exercício anterior conforme o caso:
    #
    # Caso o número de lados seja inferior a 3 escrever NÃO É UM POLÍGONO.
    # Caso o número de lados seja superior a 5 escrever POLÍGONO NÃO IDENTIFICADO.

    forma = ""
    length = ""

    if lados < 3:
        forma = "NÃO É UM POLÍGONO"
    elif lados == 3:
        forma = "TRIÂNGULO"
        length = tamanho * 3
    elif lados == 4:
        forma = "QUADRADO"
        length = tamanho * 4
    elif lados == 5:
        forma = "PENTÁGONO"
    else:
        forma = "POLÍGONO NÃO IDENTIFICADO"

    return forma + str(length)


def ex9(val1, val2, val3):
    # Escreva um programa para ler 3 valores inteiros e escrever o maior deles. Considere que o usuário não informará
    # valores iguais.

    a = val1
    b = val2
    c = val3

    if a > b:
        aux = b
        b = a
        a = aux
        # agora sei que a é menor que b

    if b > c:
        aux = c
        c = b
        b = aux

    if a > b:
        aux = b
        b = a
        a = aux
        # agora sei que a é menor que b

    if a > c:
        aux = c
        c = a
        a = aux
        # agora eu sei que a é o menor número

    return c


# Escreva um programa que leia as medidas dos lados de um triângulo e escreva se ele é Equilátero, Isósceles ou
# Escaleno. Sendo que:
# Triângulo Equilátero: possui os 3 lados iguais. Triângulo Isósceles: possui 2 lados iguais.
# Triângulo Escaleno: possui 3 lados diferentes.
def ex10(lado1, lado2, lado3):
    if lado1 == lado2 and lado1 == lado3:
        return "Equilátero"
    elif lado1 == lado3 or lado1 == lado2 or lado2 == lado3:
        return "Isosceles"
    else:
        return "Escaleno"


# Escreva um programa que leia o valor de 3 ângulos de um triângulo e escreva se o triângulo é Acutângulo,
# Retângulo ou Obtusângulo. Sendo que: Triângulo Retângulo: possui um ângulo reto. (igual a 90º) Triângulo
# Obtusângulo: possui um ângulo obtuso. (maior que 90º) Triângulo Acutângulo: possui três ângulos agudos. (menor que
# 90º)
def ex11(ang1, ang2, ang3):
    if ang1 + ang2 + ang3 != 180:
        return "Não"

    if ang1 == 90 or ang2 == 90 or ang3 == 90:
        return "Retângulo"
    elif ang1 > 90 or ang2 > 90 or ang3 > 90:
        return "Obtuso"
    else:
        return "Agudo"
