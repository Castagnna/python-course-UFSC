# Dados os valores a, b e c de uma equação quadrática,
# implementar um programa que obtenha estes três valores (nesta ordem)
# e imprima o valor das raízes reais desta equação,
# correspondentes à soma e à subtração na fórmula de Bahskara.

def bahskara():
    """
    Calculo das raizes da equacao do segundo grau
    :return: (x1, x2)
    """
    cte = {
        'a':float(input('valor de A: ')),
        'b':float(input('valor de B: ')),
        'c':float(input('valor de C: '))
        }
    delta = cte['b']**2 - 4*cte['a']*cte['c']
    print(cte)
    print(f'delta: {delta}')
    if delta == 0:
        x1 = x2 = (-cte['b']) / (2*cte['a'])
    elif delta > 0:
        x1 = (-cte['b'] + delta**(0.5)) / (2*cte['a'])
        x2 = (-cte['b'] - delta**(0.5)) / (2*cte['a'])
    else:
        print('Raizes imaginárias')
        return None
    return x1, x2

raizes = bahskara()
print(f'Raizes: {raizes}')