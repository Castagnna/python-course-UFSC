tamanho = int(input('tamanho: '))

for i in range(tamanho):
    n = int(input(f'n{i+1}: '))
    if i == 0:
        menor = n
    elif n < menor:
        menor = n
print(menor)