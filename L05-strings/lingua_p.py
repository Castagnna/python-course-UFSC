p_texto = 'pA pppapppa pdpo pPpapppa'

p_palavras = p_texto.split()
print(p_palavras)

novas_palavras = []
for p_palavra in p_palavras:
    palavra_sem_p = ''
    for posicao, letra in enumerate(p_palavra):
        if posicao % 2 == 1:
            palavra_sem_p += letra
    novas_palavras.append(palavra_sem_p)

print(' '.join(novas_palavras))