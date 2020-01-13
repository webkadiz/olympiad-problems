n = int(input())

s = {str(i) for i in range(1, n + 1)}

def comb(rest = s, res = ''):

	if not rest:
		print(res)

	for el in sorted(rest):
		comb(rest - { el }, res + el)

comb()