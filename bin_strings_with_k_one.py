n, k = map(int, input().split())

def bin_str(n, am = 0, res = ''):
	global k

	if am > k: return
	elif n + am < k: return
	elif am == k:
		print(res + '0' * n)
		return
	elif not n: return
	else:
		bin_str(n - 1, am, res + '0')
		bin_str(n - 1, am + 1, res + '1')

bin_str(n)

