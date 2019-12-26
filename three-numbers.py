a, b, c = map(int, input().split(' '))


if a * b == c:
	print('Yes')
	print(a, b, c)
elif b * c == a:
	print('Yes')
	print(b, c, a)
elif a * c == b:
	print('Yes')
	print(a, c, b)
else:
	print('No')


