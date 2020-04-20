def cavalo(cord1, cord2):
    add = [
        [1, 2],
        [1, -2],
        [-1, 2],
        [-1, -2],
        [2, 1],
        [2, -1],
        [-2, 1],
        [-2, -1],
    ]

    possibilidades = []
    for i in range(len(add)):
        ponto = [c1 + c2 for c1, c2 in zip(add[i], cord1)]
        if sum([(1 <= a <= 8) for a in ponto]) == 2:
            possibilidades.append(ponto)
        else:
            pass
    print(f'\nPossibilidades: {possibilidades}')

    resultado = False
    for i in range(len(possibilidades)):
        if cord2 == possibilidades[i]:
            resultado = True
            break
    return resultado

pontos = [[],[]]
for i in range(2):
    for j in range(2):
        while True:
            valor = int(input(f'Ponto {i+1}, a{j+1}: '))
            if 1 <= valor <= 8:
                pontos[i].append(valor)
                break
            else:
                print('Valor deve estar em [1,8]!')

print(f'Print: {pontos}')
r = cavalo(pontos[0], pontos[1])
print('é possível' if r else 'Nao é possivel')