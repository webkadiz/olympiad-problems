n = 6
a = []
k = 1000

for i in range(n):
	a.append(int(input()))

for i in range(n):
	j = a[i] // 10 % 10

	if (j == a[i] % 10 or j == a[i] // 100 or a[i] % 10 == a[i] // 100) and a[i] < k:
		k = a[i]

print('===')
for i in range(n):
	j = a[i] // 10 % 10

	if (j == a[i] % 10 
				or j == a[i] // 100 or a[i] % 10 == a[i] // 100):
		a[i] = k

	print(a[i])
