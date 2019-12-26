import math

mes = input()

lmes = len(mes)
middle = math.ceil(len(mes) / 2)

found = ''

for i in range(middle, lmes - 1):

	left = mes[:i]
	right = mes[lmes - i:]

	if left == right and len(left) + len(right) > lmes:
		found = left
		break

if found:
	print('YES')
	print(found)
else:
	print('NO')

