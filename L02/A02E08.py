def Fgaloes(area):
    litro_por_galao = 3.6
    preco_por_galao = 25.0
    area_por_litro = 18
    litros = area/area_por_litro
    galoes = round(litros / litro_por_galao)
    if galoes == 0:
        galoes += 1
    else:
        pass
    valor = galoes*preco_por_galao
    return area, galoes, valor


a = float(input('Digite a area em m2: '))
r = Fgaloes(a)
print('\n' + 40*'=')
print(f'- área de cobertura : {r[0]} m2')
print(f'- Numero de galoes : {r[1]}')
print(f'- Valor a ser pago : R$ {r[2]:.2f}')
print(40*'=')