




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




m = int(input())
n = int(input())


sqrtN = int(pow(n, 0.5)) + 1

print(sqrtN)

if sqrtN > m:

	print('common')

	real_pr = common_sieve(n)

else:
	print('secondary')

	primes = common_sieve(sqrtN)

	sieve = [True] * (n - m + 1)

	for prime in primes:

		h = m % prime

		print(h, prime - h, prime)

		j = 0 if h == 0 else prime - h

		for t in range(j, n - m + 1, prime):
			sieve[t] = False


	real_pr = []

	for i in range(n - m + 1):

		if sieve[i]:
			real_pr.append(i + m)




# print(real_pr)