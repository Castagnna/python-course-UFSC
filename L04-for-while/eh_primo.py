# def eh_primo(n):
#     if n <= 1 or n % 2 == 0:
#         return False
#     divisores = range(3, n, 2)
#     for divisor in divisores:
#         print(divisores)       
#         if n % divisor == 0:
#             return False
#         divisores = list(set(divisores) - set(range(divisor, n, divisor)))
#         if len(divisores) == 0:
#             return False
#     return True


def eh_primo(n):
    if n <= 1 or n % 2 == 0:
        return False
    limite = int(n**0.5) + 1
    divisores = range(3, limite, 2)
    while len(divisores) > 0:
        print(divisores)       
        if n % divisores[0] == 0:
            return False
        divisores = list(set(divisores) - set(range(divisores[0], n, divisores[0])))
    return True


print(eh_primo(1013))