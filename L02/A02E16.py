def dist_2p(p1, p2):
    distancia = ((p2[0] - p1[0])**2 + (p2[1] - p1[1])**2)**0.5
    return distancia


coord = ('x', 'y')
pontos = []
for i in range(2):
    p = []
    for letra in range(len(coord)):
        p.append(float(input(f'{coord[letra]}{i}: ')))
    pontos.append(p)

print(pontos)
print(f'Distancia : {dist_2p(pontos[0], pontos[1])}')