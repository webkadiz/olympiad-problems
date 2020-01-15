n, m = map(int, input().split())

arr = [[0] * (m + 1) for i in range(n + 1)]

arr[0][1] = 1


import sys

print(sys.getsizeof(arr) / 1024 / 1024)

for i in range(1, n + 1):
	for j in range(1, m + 1):
		arr[i][j] = arr[i - 1][j] + arr[i][j - 1]

print(arr[n][m])