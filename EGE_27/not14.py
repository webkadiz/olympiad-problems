# Условие задачи
# https://inf-ege.sdamgia.ru/problem?id=15867

n = int(input())
k=k1=k2=k7=k14=0
x = int(input())

for i in range(n-1):
	if x % 14 == 0: k14 += 1
	elif x % 7 == 0: k7 += 1
	elif x % 2 == 0: k2 += 1
	else: k1 += 1

	x = int(input())

	if x % 7 == 0:
		k += k1
		k += k7
	elif x % 2 == 0:
		k += k1
	else:
		k += k2
		k += k1

print(k) 