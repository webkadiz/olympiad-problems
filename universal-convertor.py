n = int(input('Из чего переводить: '))
x = input('Что переводить: ')
k = int(input('Куда переводить: '))

x10 = int(x, n)

ans = '' if x10 else '0'

while x10 > 0:
	digit = x10 % k

	if digit >= 10:
		digit = chr(55 + digit)

	ans = str(digit) + ans
	x10 //= k

print(ans)  