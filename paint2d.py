a, b = map(int, input().split())

a,b = min(a,b), max(a,b)

dp = [[4, 6] + [0] * (b - 2) for i in range(a)]


for i in range(1, b):
	




k = [4, 6] + [0] * (n - 2)

for i in range(2, n):

	if i % 2:
		k[i] = k[i//2] + 4
	else:
		k[i] = k[i-1] + 2

res = k[n-1]

print(res)

