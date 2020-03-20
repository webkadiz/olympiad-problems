# Условие задачи
# https://inf-ege.sdamgia.ru/problem?id=15995

n = int(input())
m = 5
win = [0] * m
k=k1=k2=k13=k26=0

for i in range(m):
	win[i] = int(input())

for i in range(n-m):
	x = win[i%m]

	if x % 26 == 0: k26 += 1
	elif x % 13 == 0: k13 += 1
	elif x % 2 == 0: k2 += 1
	else: k1 += 1

	x = int(input())
	win[i%m] = x

	if x % 26 == 0: k += k26 + k13 + k2 + k1
	elif x % 13 == 0: k += k26 + k13 + k2 + k1
	elif x % 2 == 0: k += k26 + k13
	else: k += k26 + k13

print(k)