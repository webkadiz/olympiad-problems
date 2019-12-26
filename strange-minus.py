number, k = map(int, input().split(' '))

for i in range(k):
	right_digit = number % 10

	if right_digit != 0:
		number -= 1
	else:
		number //= 10

print(number)