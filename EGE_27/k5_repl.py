k = 10001
n = 6
a = []

for i in range(n):
	a.append(int(input()))

for i in range(n):
	if a[i] % 5 == 0 and a[i] < k:
		k = a[i]

for i in range(n):
	if a[i] % 5 == 0:
		a[i] = k
	print(a[i], end=" ")