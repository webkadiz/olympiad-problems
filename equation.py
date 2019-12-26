import math
import timeit
import random

n = int(input())

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


print(primes)

# while not found:

# 	a = random.randint(n + 1, n + 10**7)

# 	b = a - n


# 	if not primes[a] and not primes[b]:
# 		found = True



# print(a, b)