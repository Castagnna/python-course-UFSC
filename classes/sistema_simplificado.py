import math

class FichaBancaria:

    def __init__(self):
        self.__numero = 0
        self.__nome = ''
        self.__cpf = ''
        self.__saldo = 0
        self.__situacao = 'ativada'

    def get_numero(self):
        return self.__numero

    def get_nome(self):
        return self.__nome[:]

    def get_cpf(self):
        return self.__cpf

    def get_saldo(self):
        return self.__saldo

    def get_situacao(self):
        return self.__situacao[:]

    def set_numero(self, numero_conta):
        self.__numero = numero_conta

    def set_cpf(self, cpf):
        self.__cpf = cpf

    def set_nome(self, nome):
        self.__nome = nome

    def set_situacao(self, situacao):
        self.__situacao = situacao

    def debite(self, valor):
        self.__saldo -= valor

    def credite(self, valor):
        self.__saldo += valor


class Banco:

    def __init__(self, nome_banco, codigo_banco):
        self.__nome = nome_banco
        self.__numero = codigo_banco
        self.__fichario = {}

    def get_nome(self):
        return self.__nome[:]

    def get_contas(self):
        return self.__fichario.keys()

    def abre_conta(self, cpf_cliente, nome_cliente):
        ''' Abre uma nova conta no banco '''

        ficha = FichaBancaria()
        ficha.set_numero(int(cpf_cliente))
        ficha.set_nome(nome_cliente)
        ficha.set_cpf(int(cpf_cliente))
        self.__fichario[int(cpf_cliente)] = ficha

        return True, ficha.get_nome(), ficha.get_numero()

    def deposito(self, numero_conta, valor):
        ''' Realiza um depósito numa conta '''

        if numero_conta in self.__fichario:
            self.__fichario[numero_conta].credite(valor)
            return True
        else:
            return False

    def saque(self, numero_conta, valor):
        ''' Realiza um saque numa conta '''

        if numero_conta in self.__fichario:
            self.__fichario[numero_conta].debite(valor)
            return True
        else:
            return False

    def transferencia(self, nct_origem, nct_destino, valor):
        ''' Realiza transferência entre duas contas '''

        if nct_origem not in self.__fichario:
            return False, "Conta de origem não existe"
        if nct_destino not in self.__fichario:
            return False, "Conta de destino não existe"

        ficha_origem = self.__fichario[nct_origem]
        ficha_destino = self.__fichario[nct_destino]

        ficha_origem.debite(valor)
        ficha_destino.credite(valor)

        return True, "Transferencia realizada com sucesso"

    def saldo(self, numero_conta):
        ''' Obtém o saldo de uma conta '''

        if numero_conta in self.__fichario:
            return self.__fichario[numero_conta].get_saldo()
        else:
            return False

# main

banco = Banco("Banco UFSC", 1)

operacoes = {
    "abre_conta": banco.abre_conta,
    "deposito": banco.deposito,
    "transferencia": banco.transferencia,
    "saque": banco.saque,
}

while True:
    try:
        entrada = [float(i) if i.replace(".", "", 1).isdigit() else i for i in input().split()]
        operacao = operacoes[entrada[0]]
        operacao(*entrada[1:])
    except EOFError:
        break
    except KeyboardInterrupt:
        break

contas = sorted(banco.get_contas())
for conta in contas:
    print("{} {:.2f}".format(conta, banco.saldo(conta)))