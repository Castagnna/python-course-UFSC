# Seja 'p' um numero Natural, # se não houver nenhum divisor  de 'p' no intervalo [2, raiz(n)], então 'p' é primo.


def gerador_de_primos(n):
    numeros = range(3, n+1, 2)
    primos = []
    while len(numeros) > 0:
        numero = numeros[0]
        novo_set = set(numeros) - set(range(numero, n+1, numero))
        numeros = sorted(novo_set)
        primos.append(numero)
    return primos


def contar_primos_entre(xi, xf):
    primos = gerador_de_primos(xf)
    primos_no_intervalo = [n for n in primos if xi <= n <= xf]
    return len(primos_no_intervalo)


xi = int(input('xi: '))
xf = int(input('xf: '))
# print(gerador_de_primos(xf))
print(contar_primos_entre(xi, xf))

