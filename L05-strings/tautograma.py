def eh_tautograma(texto):
    texto = texto.lower()
    palavras = texto.split()
    primeira_letra = texto[0]

    return all(primeira_letra in palavra[0] for palavra in palavras)

while True:
    texto = input().lower()
    if texto == '*':
        break
    print('Y' if eh_tautograma(texto) else 'N')