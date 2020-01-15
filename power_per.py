import timeit

res = timeit.repeat(
'''

n = 999999998

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
sqrtN = int(pow(n, 0.5)) + 1

maxDiv = max(factor_n.keys())

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
		break



'''
, number=1, repeat=3)

print(res)