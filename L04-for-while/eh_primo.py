# Seja 'n' um numero natural,
# se 'n' não for primo então terá ao menos um divisor no intervalor de [2 , raiz(N)]

# Seja 'p' um numero Natural,
# se não houver nenhum divisor  de 'p' no intervalo [2, raiz(n)], então 'p' é primo.


def eh_primo(n):
    if n <= 1 or n % 2 == 0:
        return False
    limite = int(n ** 0.5) + 1
    divisores = range(3, limite, 2)
    while len(divisores) > 0:
        divisor = divisores[0]
        if n % divisor == 0:
            return False
        divisores = list(set(divisores) - set(range(divisor, limite, divisor)))
    return True


def contar_primos_entre(xi, xf):
    intervalo = range(xi, xf + 1)
    return sum([eh_primo(n) for n in intervalo])


print(eh_primo(1013))