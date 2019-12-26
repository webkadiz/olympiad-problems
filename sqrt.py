

def sqrt(num):
	precision = 0.00000000000001

	left = bool(num)
	right = num

	middle = (left + right) / 2

	approx = middle * middle

	while abs(num - approx) > precision:

		print(approx, middle)

		if approx > num:
			right = middle
		else:
			left = middle

		middle = (left + right) / 2

		approx = middle * middle

	return middle



def isPrime(num):


	prime = True

	start = 2

	while start <= num / start:

		print(start, num / start)

		if not num % start:
			prime = False

		start += 1

	return prime


print(isPrime(17))