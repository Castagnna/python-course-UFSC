n_bandejas = int(input('n_bandejas: '))

latas_copos = [input('[L C]: ') for i in range(n_bandejas)]

quebrados = 0
for lata_copo in latas_copos:
	n_latas, n_copos = [int(x) for x in lata_copo.split()]
	if n_latas > n_copos:
		quebrados += n_copos
print(quebrados)