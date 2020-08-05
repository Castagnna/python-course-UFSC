def metodo_euclides(n1, n2):
    while True:
        resto = n1 % n2
        n1 = n2
        n2 = resto
        if resto == 0:
            return n1


print(metodo_euclides(60, 40))