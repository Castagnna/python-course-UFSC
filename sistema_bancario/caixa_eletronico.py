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

    def valor_total_em_caixa(self):
        valor = 0
        for cedula, qtd in self.__cedulas_e_qtd.items():
            valor += cedula*qtd
        return valor

    def saque(self, numero_conta, valor):
        return self.__banco.saque(numero_conta, valor)

    def deposito(self, numero_conta, valor):
        return self.__banco.deposito(numero_conta, valor)

    def mostra_situacao_da_conta(self, numero_conta):
        return self.__banco.mostra_situacao_da_conta(numero_conta)

    def transferencia(self, nct_origem, nct_destino, valor):
        return self.__banco.transferencia(nct_origem, nct_destino, valor)

    def saldo(self, numero_conta):
        return self.__banco.saldo(numero_conta)

    def tenta_sacar(self, valor):

        qtd_cedulas_distintas_no_caixa = len(self.__cedulas_e_qtd)

        cedulas_no_caixa = sorted(self.__cedulas_e_qtd.keys())

        qtd_de_cedulas_do_saque = [0] * qtd_cedulas_distintas_no_caixa

        for i in range(qtd_cedulas_distintas_no_caixa - 1, -1, -1):
            cedula = cedulas_no_caixa[i]
            qtd_de_cedulas_do_saque[i] = int(min(valor // cedula, self.__cedulas_e_qtd[cedula]))
            self.__cedulas_e_qtd[cedula] -= qtd_de_cedulas_do_saque[i]
            valor -= cedula * qtd_de_cedulas_do_saque[i]

        valor_restante = valor
        if valor_restante == 0:
            saque = [[nota, qtd] for nota, qtd in zip(cedulas_no_caixa, qtd_de_cedulas_do_saque) if qtd > 0]
            return True, saque, valor_restante
        else:
            return False, [None], valor_restante

    def saque_de_cedulas(self, numero_conta, valor):

        if self.saldo(numero_conta) < valor:
            return False, "Saldo insuficiente"

        valor_em_caixa = self.valor_total_em_caixa()
        if valor_em_caixa < valor:
            return False, "Saque maior que o valor total em caixa. Limite do saque {}".format(valor_em_caixa)

        saque_valido, saque, valor_restante = self.tenta_sacar(valor)
        if not saque_valido:
            return False, "Notas disponiveis não fecham com o valor do saque, diferença: R$ {}.".format(valor_restante)

        self.__banco.saque(numero_conta, valor)

        return True, saque
