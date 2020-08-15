class CaixaEletronico:

    cedulas = [2, 5, 10, 20, 50, 100]

    def __init__(self, banco, codigo_do_caixa, qtd_de_cada_cedula=5):
        self.__banco = banco
        self.__codigo = codigo_do_caixa
        self.__qtd_cedulas = [qtd_de_cada_cedula] * len(self.cedulas)

    def get_situacao_do_caixa(self):
        return [[cedula, qtd] for cedula, qtd in zip(self.cedulas, self.__qtd_cedulas)]

    def cx_saque(self, numero_conta, valor):
        return self.__banco.saque(numero_conta, valor)

    def cx_deposito(self, numero_conta, valor):
        return self.__banco.deposito(numero_conta, valor)

    def cx_verifica_situacao(self, numero_conta):
        return self.__banco.verifica_situacao(numero_conta)

    def cx_transferencia(self, nct_origem, nct_destino, valor):
        return self.__banco.transferencia(nct_origem, nct_destino, valor)

    def cx_saldo(self, numero_conta):
        return self.__banco.saldo(numero_conta)

    def cx_saque_de_cedulas(self, numero_conta, valor):

        status_da_operacao = self.__banco.saque(numero_conta, valor)

        qtd_cedulas_distintas = len(self.cedulas)

        if status_da_operacao:
            qtd_de_cedulas_do_saque = [0] * qtd_cedulas_distintas

            for i in range(qtd_cedulas_distintas - 1, -1, -1):

                qtd_de_cedulas_do_saque[i] = int(min(valor // self.cedulas[i], self.__qtd_cedulas[i]))
                valor -= self.cedulas[i] * qtd_de_cedulas_do_saque[i]

            return True, [[cedula, qtd] for cedula, qtd in zip(self.cedulas, qtd_de_cedulas_do_saque)]

        else:
            return False, [None]
