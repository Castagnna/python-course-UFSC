def price(days, km):
    fc = 45
    km_limit_day = 60
    rs_km = 0.50
    saldo = km - km_limit_day*days
    if saldo < 0:
        saldo = 0

    value = days*fc + rs_km*(saldo)
    return value

print(price(10, 700))

