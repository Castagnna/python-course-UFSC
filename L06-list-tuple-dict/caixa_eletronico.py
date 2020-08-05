n_celudas_diferentes = int(input())
caixa = {}
for i in range(n_celudas_diferentes):
    cedula = float(input())
    qtd_da_cedula = int(input())
    caixa[cedula] = qtd_da_cedula
# print(caixa)

saque = float(input())

cedulas_do_saque = {}
for cedula in sorted(caixa.keys(), reverse=True):
    cedulas_do_saque[cedula] = 0
    while cedula <= saque and caixa[cedula] > 0:
        saque -= cedula
        caixa[cedula] -= 1
        cedulas_do_saque[cedula] += 1

str_list = [str(cedulas_do_saque[cedula]) for cedula in sorted(cedulas_do_saque.keys())]
print(' '.join(str_list))
