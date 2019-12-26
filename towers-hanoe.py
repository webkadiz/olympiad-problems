import time

n = int(input())


def move(n, x, y):
	m = 6 - (x + y)

	if n == 1:
		return print(n, x, y)

	move(n - 1, x, m)
	print(n, x, y)
	move(n - 1, m, y)

move(n, 1, 3)