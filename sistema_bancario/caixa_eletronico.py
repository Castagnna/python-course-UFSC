class CaixaEletronico:

    def __init__(self, banco, codigo_do_caixa):
        self.__banco = banco
        self.__codigo = codigo_do_caixa
        self.__cedulas_e_qtd = {}

    def abastece_o_caixa(self, cedulas_quantidades):

        if not isinstance(cedulas_quantidades, dict):
            return False, "Falha, dados de entrada não são do tipo dicionario"

        for cedula, qtd in cedulas_quantidades.items():
            if cedula in self.__cedulas_e_qtd:
                self.__cedulas_e_qtd[cedula] += qtd
            else:
                self.__cedulas_e_qtd[cedula] = qtd

        return True, "Caixa abastecido"

    def mostra_cedulas_e_quantidades(self):
        return [[cedula, self.__cedulas_e_qtd[cedula]] for cedula in sorted(self.__cedulas_e_qtd.keys())]

    def saque(self, numero_conta, valor):  # retirar o cx da frente do saque
        return self.__banco.saque(numero_conta, valor)

    def deposito(self, numero_conta, valor):
        return self.__banco.deposito(numero_conta, valor)

    def mostra_situacao_da_conta(self, numero_conta):
        return self.__banco.mostra_situacao_da_conta(numero_conta)

    def transferencia(self, nct_origem, nct_destino, valor):
        return self.__banco.transferencia(nct_origem, nct_destino, valor)

    def saldo(self, numero_conta):
        return self.__banco.saldo(numero_conta)

    def verifica_cedulas_para_o_saque(self, valor):
        return True

    def saque_de_cedulas(self, numero_conta, valor):

        if not self.verifica_cedulas_para_o_saque(valor):
            return False, "Quantidade de cedulas insuficiente para o saque"

        if self.saldo(numero_conta) < valor:
            return False, "Saldo insuficiente"

        self.__banco.saque(numero_conta, valor)

        qtd_cedulas_distintas = len(self.__cedulas)

        qtd_de_cedulas_do_saque = [0] * qtd_cedulas_distintas

        for i in range(qtd_cedulas_distintas - 1, -1, -1):
            qtd_de_cedulas_do_saque[i] = int(min(valor // self.__cedulas[i], self.__qtd_de_cada_cedula_do_caixa[i]))
            self.__qtd_de_cada_cedula_do_caixa[i] -= qtd_de_cedulas_do_saque[i]
            valor -= self.__cedulas[i] * qtd_de_cedulas_do_saque[i]

        return True, [[cedula, qtd] for cedula, qtd in zip(self.__cedulas, qtd_de_cedulas_do_saque) if qtd > 0]

