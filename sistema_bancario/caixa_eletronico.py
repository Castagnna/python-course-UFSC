class CaixaEletronico:

    def __init__(self, banco, codigo_do_caixa):
        self.__banco = banco
        self.__codigo = codigo_do_caixa

    def cx_saque(self, numero_da_conta, valor):
        return self.__banco.saque(numero_da_conta, valor)

    def cx_deposito(self, numero_da_conta, valor):
        return self.__banco.deposito(numero_da_conta, valor)
