data = list(map(int, input().split()))

m = data.pop(0)
n = data.pop(0)

ves = []
rows = []


def bin_search(el, arr):
	left = -1
	right = len(arr)

	while right - left > 1:
		m = (left + right) // 2
		if arr[m] > el:
			right = m
		else: 
			left = m

	return right

for i in range(n):
	row = data[i*m:i*m+m]
	row = sorted(row, reverse=True)
	exp = sum(row)

	idx = bin_search(exp, ves)

	ves.insert(idx, exp)
	rows.insert(idx, row)

[print(*row, end=' ') for row in rows]
