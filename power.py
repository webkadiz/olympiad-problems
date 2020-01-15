n = int(input())

if n == 1:
	print(1)
	exit()

def factor_dict(n):

	d={}

	sqrtN = int(pow(n, 0.5)) + 1

	for i in range(2, sqrtN):

		while not n % i:
			if i in d: d[i] += 1
			else: d[i] = 1

			n //= i

	if n != 1:
		d[n] = 1

	return d

factor_n = factor_dict(n)
keys = list(factor_n.keys())
sqrtN = int(pow(n, 0.5)) + 1

maxDiv = max(keys)

if len(keys) > 1:
	keys.remove(maxDiv)
	maxDiv2 = max(keys)


	if maxDiv2 > 500:
		maxDiv *= maxDiv2

for i in range(maxDiv, 10 ** 9, maxDiv):
	factor_cur = factor_dict(i)

	for k in factor_cur:
		factor_cur[k] *= i

	for k in factor_n:
		if k not in factor_cur:
			factor_cur[k] = 0

	for k in factor_n:
		factor_cur[k] -= factor_n[k]


	len_f_c = len(factor_cur)
	am = 0
	for k in factor_cur:
		if factor_cur[k] >= 0: am += 1

	
	if am == len_f_c:
		print(i)
		exit()


