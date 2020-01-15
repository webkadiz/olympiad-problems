n = int(input())


sqrtN = int(pow(n, 0.5)) + 1


def test_ferma(n):

	import random
	from math import gcd

	i = 0
	while i < 100:
		rand = random.randint(1, pow(10, 6))

		if gcd(n, rand) != 1:
			continue

		if pow(rand, n - 1, n) != 1:
			return False

		i += 1

	return True


res = test_ferma(n)

if res:
	print('prime')
else:
	print('composite')



