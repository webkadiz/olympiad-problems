n, k = map(int, input().split())



k = 0
ld = 1
for i in range(2, n + 1):
	ld = ld * i

	t = str(ld)

	while int(t[-1]) == 0:
		k += 1
		t = t[:-1]

	print(ld, t, end=' ')
	ld = int(t[-1])
	print(ld)

print(ld, k)
