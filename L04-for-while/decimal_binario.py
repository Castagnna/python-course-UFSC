# n = int(input())
n = 0
bin = ''

while True:
    bin = str(n % 2) + bin
    n = n // 2
    if n == 0:
        break

print(bin)