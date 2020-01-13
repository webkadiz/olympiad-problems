n = int(input())


def bin_str(n, res = ''):

	if not n:
		print(res)
		return

	bin_str(n - 1, res + '0')
	bin_str(n - 1, res + '1')

bin_str(n)