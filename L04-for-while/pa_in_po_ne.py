valores = [int(input()) for i in [1, 2, 3, 4, 5]]
relatorio = {
	'par': 0,
	'impar': 0,
	'positivo': 0,
	'negativo': 0
}

for valor in valores:
	if valor % 2 == 0:
		relatorio['par'] = relatorio['par'] + 1
	else:
		relatorio['impar'] = relatorio['impar'] + 1

	if valor > 0:
		relatorio['positivo'] = relatorio['positivo'] + 1
	elif valor < 0:
		relatorio['negativo'] = relatorio['negativo'] + 1

print(relatorio)