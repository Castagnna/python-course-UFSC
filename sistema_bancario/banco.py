import math
from ficha_bancaria import FichaBancaria


class Banco:
    
    def __init__(self, nome_banco, codigo_banco):
        self.__nome = nome_banco
        self.__numero = codigo_banco
        self.__fichario = {}
        self.__ultima_conta_criada = 0

    def get_nome(self):
        return self.__nome[:]
        
    def abre_conta(self, nome_cliente, cpf_cliente):
        ''' Abre uma nova conta no banco '''
        
        self.__ultima_conta_criada += 1
        
        ficha = FichaBancaria()
        ficha.set_numero(self.__ultima_conta_criada)
        ficha.set_nome(nome_cliente)
        ficha.set_cpf(cpf_cliente)
        self.__fichario[self.__ultima_conta_criada] = ficha

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

        return True, f"Transferencia realizada com sucesso"

    def saldo(self, numero_conta):
        ''' Obtém o saldo de uma conta '''
        
        if numero_conta in self.__fichario:
            return self.__fichario[numero_conta].get_saldo()
        else:
            return False

    def mostra_situacao_da_conta(self, numero_conta):
        nome = self.__fichario[numero_conta].get_nome()
        situacao = self.__fichario[numero_conta].get_situacao()
        saldo = self.saldo(numero_conta)
        return nome, situacao, saldo

    def encerra_conta(self, numero_conta):
        ''' Encerra uma conta '''
        
        if numero_conta in self.__fichario and self.saldo(numero_conta) == 0:
            self.__fichario[numero_conta].set_situacao('desativada')
            return True, f"Conta {numero_conta} desativada com sucesso"
        else:
            return False, f"Não foi possivel encerrar a conta {numero_conta}"
        
    def conta_maior_saldo(self):
        '''Obtém o nº da conta do cliente com maior saldo'''
        
        maior_saldo = -math.inf
        nct = 0
        for ficha in self.__fichario.values():
            if ficha.get_saldo() > maior_saldo:
                maior_saldo = ficha.get_saldo()
                nct = ficha.get_numero()
        return nct
    
    def saldo_medio(self):
        '''Cálcula o saldo médio dos '''
        
        soma = 0
        for ficha in self.__fichario.values():
            soma += ficha.get_saldo()
        return soma / len(self.__fichario)      
    
    def cpfs_duplicados(self):
        ''' Obtém os cpfs duplicados (em mais de uma conta) '''
        
        cpfs_duplicados = set()
        cpfs = set()
        for ficha in self.__fichario.values():
            if ficha.get_cpf() in cpfs:
                cpfs_duplicados.add(ficha.get_cpf())
            else:
                cpfs.add(ficha.get_cpf())
        return cpfs_duplicados
