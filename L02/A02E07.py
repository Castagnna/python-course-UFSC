def salario_liquido(hr, hrEx):
    valor_hr = 2500 / 200
    bruto = hr*valor_hr + hrEx*valor_hr*1.2
    ir = bruto*0.13
    inss = bruto*0.09
    liquido = bruto - ir - inss
    return bruto, ir, inss, liquido


horas = float(input('Horas Normais: '))
horas_extra = float(input('Horas Extra: '))
r = salario_liquido(horas, horas_extra)
print('\n' + 40*'=')
print(f'- Salário Bruto : R$ {r[0]:.2f}')
print(f'- IR : R$ {r[1]:.2f}')
print(f'- INSS : R$ {r[2]:.2f}')
print(f'- Salário Liquido : R$ {r[3]:.2f}')
print(40*'=')