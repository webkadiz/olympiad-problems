# Условие задачи
# https://inf-ege.sdamgia.ru/problem?id=18096

n = int(input())
k = k62 = k31 = k2 = k1 = 0

for i in range(n):
	x = int(input())

	if x % 62 == 0:
		k += k62 + k31 + k2 + k1
	elif x % 31 == 0:
		k += k62 + k2
	elif x % 2 == 0:
		k += k62 + k31
	else:
		k += k62

	if x % 62 == 0: k62 += 1
	elif x % 31 == 0: k31 += 1
	elif x % 2 == 0: k2 += 1
	else: k1 += 1

print(k)