import timeit


res = timeit.repeat(
"""
import math
import timeit
import random

n = 10000000

found = False

def primeSeq(n):
	rootN = int(math.sqrt(n)) + 1

	prime = [True] * (n + 1)
	prime[0] = prime[1] = False


	for i in range(rootN):
		if prime[i]:
			prime[i] = i
			for j in range(i*i, n + 1, i):
				prime[j] = False

	return prime



primes = primeSeq(n)

# while not found:

# 	a = random.randint(n + 1, n + 10**6*2)

# 	b = a - n


# 	if not primes[a] and not primes[b]:
# 		found = True



#print(a, b)
""", repeat=3, number=1)


print(res)
