# lista1 = [3,4,5]
# lista2 = [2,4]
#
# print(len(set(lista1) - set(lista2)))
#
# primos = [3, 5, 7,11, 13]
# primos_no_intervalo = [n for n in primos if 5 <= n <= 10]
# print(primos_no_intervalo)


lista = list(range(17, 101, 17))
print(lista)
mul = set(lista)
num = set([17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97])
print(num)
print(mul)
r = sorted(num - mul)
print(r)