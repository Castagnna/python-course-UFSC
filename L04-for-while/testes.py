# import math

# print([2] + [3])

# a = [False, None]
# print(any(a))

# print(dir())

# print('historic'[-1:5])

# dicio = {"a" : 1, "b": 2, "c": 3}
# str_list = [str(x) for x in dicio.values()][::-1]
# print(' '.join(str_list))

# lista = [1, 3]
# print(lista * -1)
#
# n_celudas_diferentes = int(input())
# caixa = {}
# for i in range(n_celudas_diferentes):
#     cedula = float(input())
#     qtd_da_cedula = int(input())
#     caixa[cedula] = qtd_da_cedula
# # print(caixa)
#
# saque = float(input())
#
# cedulas_do_saque = {}
# for cedula in sorted(caixa.keys(), reverse=True):
#     cedulas_do_saque[cedula] = 0
#     while cedula <= saque and caixa[cedula] > 0:
#         saque -= cedula
#         caixa[cedula] -= 1
#         cedulas_do_saque[cedula] += 1
#
# str_list = [str(cedulas_do_saque[cedula]) for cedula in sorted(cedulas_do_saque.keys())]
# print(' '.join(str_list))

# for cedula, qtd in zip(['A', 'B', 'C'], [1, 2, 3]):
#     print(cedula, qtd)
def soma(x, y, z):
    return x + y + z


def multiplica(x, y, z):
    return x + y + z


operacoes = {
    "soma": soma,
    "multiplica": multiplica,
}

operacao = operacoes["soma"]

valores = [2, 3, 5]

r = operacao(*valores)

print(r)