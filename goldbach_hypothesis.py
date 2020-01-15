
m = int(input())

def common_sieve(n):

	primes = [True] * (n + 1)
	primes[0] = primes[1] = False

	sqrtN = int(pow(n, 0.5)) + 1

	for i in range(2, sqrtN):
		if primes[i]:
			for j in range(i*i, n + 1, i):
				primes[j] = False

	return primes


am = 2 * 10 ** 5

pr = common_sieve(am)


for i in range(am + 1):

	if pr[i] and pr[m - i]:
		print(i, m - i)
		break
