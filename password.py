s = input()


params = [0, 0, 0]


if len(s) < 8:
	print('NO')
	exit()

for char in s:

	if all(params):
		break


	if 97 <= ord(char) <= 122:
		params[0] = 1

	elif 65 <= ord(char) <= 90:
		params[1] = 1

	elif 48 <= ord(char) <= 57:
		params[2] = 1


print('YES') if all(params) else print('NO')