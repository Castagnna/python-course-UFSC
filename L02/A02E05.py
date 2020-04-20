def valorFuturo(vp, p, tx):
    """
    Caculo do valor futuro
    :param VP: Valor Presente
    :param p: Periodos
    :param tx: taxa de juros
    :return: Valor futuro
    """
    vf = vp*(1+tx)**p
    return vf

vp = float(input('Insira o valor presente: R$ '))
p = float(input('Insira o numero de periodos: '))
tx = float(input('Insira a taxa em valor absoluto\n(ex: para 12% digite 0.12): '))
print(f'\nValor Futuro: R$ {valorFuturo(vp, p, tx):.2f}')