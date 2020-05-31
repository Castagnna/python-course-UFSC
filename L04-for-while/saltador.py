def medias_dos_atletas(qtd_atletas):
    medias = {}
    for i in range(qtd_atletas):
        nome = input('Nome: ')
        notas = []
        for salto in [1, 2, 3]:
            nota = float(input('Salto 0' + str(salto) + ': '))
            notas.append(nota)

        media = sum(notas)/len(notas)
        medias[nome] = media
    return medias


def vencedor(medias):
    maior_media = 0
    vencedor = ''
    for atleta, media in medias.items():
        if media > maior_media:
            maior_media = media
            vencedor = atleta
    return vencedor


qtd_atletas = int(input('Numero de atletas: '))
medias = medias_dos_atletas(qtd_atletas)
vencedor = vencedor(medias)
print(medias)
print(vencedor)