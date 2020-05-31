def tempo_ate_reducao(massa_i, massa_f=0.5):
    t = 0
    while massa_i > massa_f:
        t += 50
        massa_i /= 2
    return t

massa_i = float(input('massa inicial (g): '))
print(tempo_ate_reducao(massa_i))