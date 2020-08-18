from banco import Banco
from caixa_eletronico import CaixaEletronico

# Criando banco

itopobre = Banco("Banco Itopobre", 999)
print(f"{itopobre.get_nome()} criado com sucesso")

# Operações feitas no banco

status_da_operacao, nome, numero = itopobre.abre_conta('Joao Manoel', 123)
print(f"{nome}, conta N° {numero} criada com sucesso" if status_da_operacao else "falha na operacao")

status_da_operacao, nome, numero = itopobre.abre_conta('Maria Cristina', 456)
print(f"{nome}, conta N° {numero} criada com sucesso" if status_da_operacao else "falha na operacao")

status_da_operacao, nome, numero = itopobre.abre_conta('O Cão', 666)
print(f"{nome}, conta N° {numero} criada com sucesso" if status_da_operacao else "falha na operacao")

itopobre.deposito(numero_conta=1, valor=100)
itopobre.deposito(numero_conta=2, valor=250)
itopobre.deposito(numero_conta=3, valor=1000)
itopobre.saque(numero_conta=1, valor=50)

status_da_operacao, msg = itopobre.transferencia(nct_origem=2, nct_destino=1, valor=20)
print(msg)

saldo = itopobre.saldo(numero_conta=1)
print(f"Saldo: R$ {saldo}" if saldo else "Falha na operação")

saldo = itopobre.saldo(numero_conta=999)
print(f"Saldo: R$ {saldo}" if saldo else "Falha na operação saldo")

nome, sit, saldo = itopobre.mostra_situacao_da_conta(numero_conta=1)
print(f"Situação da conta de {nome}: {sit}, saldo: R$ {saldo}")

status_da_operacao, msg = itopobre.encerra_conta(numero_conta=2)
print(msg)

nome, sit, saldo = itopobre.mostra_situacao_da_conta(numero_conta=2)
print(f"Situação da conta de {nome}: {sit}, saldo: R$ {saldo}")

itopobre.saque(numero_conta=2, valor=saldo)
status_da_operacao, msg = itopobre.encerra_conta(numero_conta=2)
print(msg)

nome, sit_m, saldo_m = itopobre.mostra_situacao_da_conta(numero_conta=2)
print(f"Situação da conta de {nome}: {sit_m}, saldo: R$ {saldo_m}")

# Operações feitas no caixa eletronico

caixa_eletronico = CaixaEletronico(itopobre, 1)
cedulas = {100: 5, 2: 10}
caixa_eletronico.abastece_o_caixa(cedulas)
situacao_do_caixa = caixa_eletronico.mostra_cedulas_e_quantidades()
print(f"situacao do caixa: {situacao_do_caixa}")

# caixa_eletronico.cx_saque(numero_conta=1, valor=10)
# nome, sit, saldo = caixa_eletronico.cx_verifica_situacao(numero_conta=1)
# print(f"Situação da conta de {nome}: {sit}, saldo: R$ {saldo}")
#
# caixa_eletronico.cx_deposito(numero_conta=1, valor=20)
# nome, sit, saldo = caixa_eletronico.cx_verifica_situacao(numero_conta=1)
# print(f"Situação da conta de {nome}: {sit}, saldo: R$ {saldo}")
#
# status_da_operacao, msg = caixa_eletronico.cx_transferencia(nct_origem=3, nct_destino=1, valor=400)
# print(msg)
# nome, sit, saldo = caixa_eletronico.cx_verifica_situacao(numero_conta=3)
# print(f"Situação da conta de {nome}: {sit}, saldo: R$ {saldo}")
#
# nome, sit, saldo = caixa_eletronico.cx_verifica_situacao(numero_conta=1)
# print(f"Situação da conta de {nome}: {sit}, saldo: R$ {saldo}")
#
# status_da_operacao, saque = caixa_eletronico.cx_saque_de_cedulas(numero_conta=1, valor=177)
# print(f"Saque: {saque}" if status_da_operacao else "Falha no saque")
#
# nome, sit, saldo = caixa_eletronico.cx_verifica_situacao(numero_conta=1)
# print(f"Situação da conta de {nome}: {sit}, saldo: R$ {saldo}")
#
# status_da_operacao, saque = caixa_eletronico.cx_saque_de_cedulas(numero_conta=1, valor=399)
# print(f"Saque: {saque}" if status_da_operacao else "Falha no saque")
#
# nome, sit, saldo = caixa_eletronico.cx_verifica_situacao(numero_conta=1)
# print(f"Situação da conta de {nome}: {sit}, saldo: R$ {saldo}")
#
# situacao_do_caixa = caixa_eletronico.get_situacao_do_caixa()
# print(f"situacao do caixa: {situacao_do_caixa}")
