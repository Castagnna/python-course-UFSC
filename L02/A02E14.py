def consumo(distancia, litros):
    km_por_l = distancia/litros
    # km_por_l = round(distancia/litros, 3)
    return km_por_l


d = int(input('distancia [km]: '))
l = float(input('combustivel [litros]: '))
print(f'Consumo : {consumo(d, l):.3f} km/l')