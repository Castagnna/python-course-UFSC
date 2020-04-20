def VP_dado_A(A, p, tx):
    """ Caculo do valor presente (VP) dado uma série uniforme (A)
    :param VP: Valor Presente
    :param p: Periodos
    :param tx: taxa de juros
    :return: Valor futuro
    """
    r = (1+tx)**p - 1
    q = tx*(1+tx)**p
    vp = A*(r/q)
    return vp


A = float(input('Insira o valor da prestação: R$ '))
p = float(input('Insira o numero de periodos: '))
tx = float(input('Insira a taxa em valor absoluto\n(ex: para 12% digite 0.12): '))
print(f'\nValor presente: R$ {VP_dado_A(A, p, tx):.2f}')