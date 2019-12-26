
n = int(input())

a = [int(input()) for i in range(n)]

k = 0

for i in range(n):
	for j in range(i + 1, n):
		print((a[i], a[j]))
		if a[i] * a[j] % 10 == 0:
			k += 1

print(k)