# Условие задачи
# Количество пар с расстоянием 4, произведение которых делится на 3, а сумма не делится на 3

n = int(input())
m = 4
win = [0] * m
k = k1 = k2 = k3 = k23 = 0

for i in range(m):
	win[i] = int(input())

for i in range(n-m):
	pr = win[i%m]
	
	if not pr % 3 and not pr % 2:
		k23 += 1
	elif not pr % 3:
		k3 += 1
	elif not pr % 2:
		k2 += 1
	else:
		k1 += 1

	x = int(input())

	if not x % 3 and not x % 2:
		k += k1 + k2
	elif not x % 3:
		k += k1 + k2
	elif not x % 2:
		k += k3 + k23
	else:
		k += k3 + k23

	win[i%m] = x

print(k)
