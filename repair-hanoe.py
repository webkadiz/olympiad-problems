n = int(input())

k = 0

def move(n, x, y):
	global k
	m = 6 - (x + y)

	

	if n == 1:
		if m == 2:
			print(n, x, 2)
			print(n, 2, y)
			k += 2
		else:
			print(n, x, y)
			k += 1
		return

	if m == 2:
		move(n, x, 2)
		move(n, 2, y)
	else:
		move(n - 1, x, m)
		print(n, x, y)
		k += 1
		move(n - 1, m, y)






move(n, 1, 3)
print(k)