def fat(n):
    if n <= 1:
        return 1
    else:
        return n * fat(n-1)


# x! > x¹⁰  <=>  x.(x-1)! > x.x⁹  <=>  (x-1)! > x⁹
x = 1
while fat(x-1) <= x**9:
    x += 1
print(x)