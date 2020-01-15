n = int(input())

fac = [0] * (n + 1)
fac[0] = 1
fac[1] = 1

for i in range(2, n + 1):
	fac[i] = fac[i - 1] * i

print(fac[n])