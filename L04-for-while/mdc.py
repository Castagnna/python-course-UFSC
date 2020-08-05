def gerador_de_primos(valor_max):
    numeros = range(3, valor_max + 1, 2)
    primos = []
    while len(numeros) > 0:
        numero = numeros[0]
        novo_set = set(numeros) - set(range(numero, valor_max + 1, numero))
        numeros = sorted(novo_set)
        primos.append(numero)
    return primos


def mdc(n1, n2):

    if n1*n2 == 0:
        return None

    maior_n = max(n1, n2)
    divisores = [2] + gerador_de_primos(maior_n)
    divisores_comuns = []
    mdc = 1
    for divisor in divisores:
        while n1 % divisor == 0 or n2 % divisor == 0:
            if n1 % divisor == 0 and n2 % divisor == 0:
                mdc *= divisor
                divisores_comuns.append(divisor)
                n1 /= divisor
                n2 /= divisor

    return mdc, divisores_comuns


def metodo_euclides(n1, n2):
    while True:
        resto = n1 % n2
        n1 = n2
        n2 = resto
        if resto == 0:
            return n1


n1 = int(input('n1: '))
n2 = int(input('n2: '))
mdc, divisores_comuns = mdc(n1, n2)
print('divisores comuns: ', divisores_comuns)
print('Normal: ', mdc)
print('Normal: ', metodo_euclides(n2, n1))