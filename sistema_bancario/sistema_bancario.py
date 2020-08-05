import banco as B

bc = B.Banco("Meu Primeiro Banco", 999)
num_cta_joaozinho = bc.abre_conta('Joazinho', 123)
print(num_cta_joaozinho)

num_cta_mariazinha = bc.abre_conta('Mariazinha', 456)
print(num_cta_mariazinha)

bc.deposito(num_cta_joaozinho, 100)
bc.deposito(num_cta_mariazinha, 250)
bc.saque(num_cta_joaozinho, 50)
bc.transferencia(num_cta_mariazinha, num_cta_joaozinho, 20)

sit_m, saldo_m = bc.verifica_situacao(num_cta_mariazinha)
print(sit_m, saldo_m)

saldo = bc.saldo(num_cta_joaozinho)
if saldo == False:
    print("Conta inexistente")
else:
    print(f"Saldo da conta {num_cta_joaozinho} = {saldo}")
    
print(f"Saldo da conta {num_cta_mariazinha} = {bc.saldo(num_cta_mariazinha)}")

n_conta = 789
print(f"Saldo da conta {n_conta} = {bc.saldo(n_conta)}")

print(bc.encerra_conta(num_cta_mariazinha))

sit_m, saldo_m = bc.verifica_situacao(num_cta_mariazinha)
print(sit_m, saldo_m)

bc.saque(num_cta_mariazinha, saldo_m)
print(bc.encerra_conta(num_cta_mariazinha))

sit_m, saldo_m = bc.verifica_situacao(num_cta_mariazinha)
print(sit_m, saldo_m)