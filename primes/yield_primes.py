def nats(n=2):
	if n < 2:
		n=2
	yield n
	yield from nats(n+1)
    
def sieve(s):
	n = next(s)
	yield n
	yield from sieve(i for i in s if i%n != 0)

prime = sieve(nats(-1))

print(next(prime))

for i in range(5):
    print(next(prime))
    