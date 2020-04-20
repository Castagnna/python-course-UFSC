def conta_luz(kwh):
    t1, t2, t3, t4 = 0.09556, 0.16698, 0.25052, 0.27836
    c1, c2, c3 = 30, 100, 200

    if kwh > c3:
        valor = c1*t1 + (c2 - c1)*t2 + (c3 - c2)*t3 + (kwh - c3)*t4
    elif kwh > c2:
        valor = c1*t1 + (c2 - c1)*t2 + (kwh - c2)*t3
    elif kwh > c1:
        valor = c1*t1 + (kwh - c1)*t2
    else:
        valor = kwh*t1
    return valor


kwh = float(input('kwh: '))
print(round(conta_luz(kwh), 2))