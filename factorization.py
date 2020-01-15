n = int(input())
numbers = []

sqrtN = int(pow(n, 0.5)) + 1

for i in range(2, sqrtN):

	while not n % i:
		n //= i
		numbers.append(i)


if n != 1:
	numbers.append(n)


res = ''

for number in numbers:
	res += str(number) + '*'


print(res[:-1])