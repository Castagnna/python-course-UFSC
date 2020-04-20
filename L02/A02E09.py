def avaliacao(notas, pesos):
    criterio = 6
    dividendo = (
        notas[0]*pesos[0] +
        notas[1]*pesos[1] +
        notas[2]*pesos[2]
    )
    divisor = sum(pesos)
    media = dividendo / divisor
    print(f'Media: {media:.1f}')
    return (media >= criterio)


notas = []
pesos = []
for i in range(3):
    while True:
        n = float(input(f'Digite a nota {i+1}/3: '))
        if 0 <= n <= 10:
            notas.append(n)
            break
        else:
            print('valor inesperado!')
for i in range(3):
    while True:
        p = float(input(f'Digite o peso {i+1}/3: '))
        if 0 <= p:
            pesos.append(p)
            break
        else:
            print('valor inesperado!')

print(f'Notas: {notas}')
print(f'Pesos: {pesos}')
print('Aprovado' if avaliacao(notas, pesos) else 'Reprovado')