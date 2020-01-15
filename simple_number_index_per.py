import timeit

res = timeit.repeat(
'''

def common_sieve(n):

	primes = [True] * (n + 1)
	primes[0] = primes[1] = False

	sqrtN = int(pow(n, 0.5)) + 1

	for i in range(2, sqrtN):
		if primes[i]:
			for j in range(i*i, n + 1, i):
				primes[j] = False

	pr = []

	for i in range(n + 1):
		if primes[i]:
			pr.append(i)

	return pr




# n = 10 ** 8

# sqrtN = int(pow(n, 0.5)) + 1

# primes = []

# print(sqrtN)

# for number in range(2, sqrtN):

# 	sqrtNumber = int(pow(number, 0.5)) + 1

# 	for j in range(2, sqrtNumber):
# 		if not number % j:
# 			break
# 	else:
# 		primes.append(number)

common_sieve(10000)

'''
, number=1, repeat=3)


print(res)