texto = 'Caio-init-bug-bing-love'.lower()
palavras = texto.split('-')


eh_cobol = all(letra in palavra[0] + palavra[-1] for palavra, letra in zip(palavras, 'cobol'))

print('GRACE HOPPER' if eh_cobol else 'BUG')
