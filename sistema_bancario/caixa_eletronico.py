class CaixaEletronico:

    def __init__(self, banco, codigo_do_caixa):
        self.__banco = banco
        self.__codigo = codigo_do_caixa

    def cx_saque(self, numero_conta, valor):
        return self.__banco.saque(numero_conta, valor)

    def cx_deposito(self, numero_conta, valor):
        return self.__banco.deposito(numero_conta, valor)

    def cx_verifica_situacao(self, numero_conta):
        return self.__banco.verifica_situacao(numero_conta)

    def cx_transferencia(self, nct_origem, nct_destino, valor):
        return self.__banco.transferencia(nct_origem, nct_destino, valor)