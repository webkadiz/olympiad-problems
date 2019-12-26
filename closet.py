s = input()


x = y = k = 0


def is_digit(digit):
	try:
		float(digit)
		return True
	except:
		return False

print(is_digit('-2.3'))

for char in s:

	if char == 'N': y += k
	elif char == 'S': y -= k
	elif char == 'E': x += k
	elif char == 'W': x -= k

	if is_digit(char):
		k = k * 10 + int(char)
	else:
		k = 0

if y:
	print(abs(y), 'S' if y < 0 else 'N', sep='', end='')

if x:
	print(abs(x), 'W' if x < 0 else 'E', sep='', end='') 