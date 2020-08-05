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
        return self.__nome
    
    def get_cpf(self):
        return self.__cpf
    
    def get_saldo(self):
        return self.__saldo

    def get_situacao(self):
        return self.__situacao
    
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