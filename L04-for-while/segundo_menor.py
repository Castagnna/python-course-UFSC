tamanho = int(input('tamanho: '))
seq = []
for i in range(tamanho):
    n = float(input(f'n{i+1}: '))
    seq.append(n)

print(sum(seq)/len(seq))