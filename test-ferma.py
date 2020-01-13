import random
import math

n = int(input())


def test_ferma(n):
	if n <= 1:
		return False

	r = 10 ** 6

	i = 0

	while i < 100:
		rand = random.randint(1, r)

		if math.gcd(n, rand) != 1:
			continue

		if rand ** (n - 1) % n != 1:
			return False

		i += 1

	return True



print(test_ferma(n))