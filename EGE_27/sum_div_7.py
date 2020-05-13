# Условие задачи
# https://inf-ege.sdamgia.ru/problem?id=14713 

n = int(input())
m = 7
en = [0] * m
k = 0

for i in range(n):
	x = int(input())
	rest = x % m

	if rest == 0: y = en[0]
	else: y = en[m-rest]
	
	k += y
	en[rest] += 1

print(k)
