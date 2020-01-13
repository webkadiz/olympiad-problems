n = int(input())


def div_slug(n, top = n, res = []):

	if n < 0:
		return
	elif n == 0:
		print(*res)
		return

	for i in range(top, 0, -1):
		div_slug(n - i, i, res + [i])


div_slug(n)