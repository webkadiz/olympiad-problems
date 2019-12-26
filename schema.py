
for n in range(200):
	beg = n
	s = 2
	r = 0

	while n > 0:
		k = 0

		while s ** k <= n:
			k += 1

		r += 10 ** (k-1)
		n -= s ** (k-1)


	if r == 10110111:
		print('yes', beg)
	else:
		print(r)