from math import log10

n = -20.026

log = log10(abs(n))
print(log)

fator = log // 1
print(fator)

novo_n = n * 10**(-fator)
print(novo_n)

sinal1 = '+' if n >= 0 else '-'
numero = str(abs(round(novo_n, 4))).ljust(6, '0')
sinal2 = 'E+' if abs(n) >= 1 else 'E-'
pot = str(abs(-fator)).rjust(2, '0')
print(sinal1 + numero + sinal2 + pot)