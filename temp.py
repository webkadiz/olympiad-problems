n = int(input())

first = second = 0

ends = [0] * 80

for i in range(n):
	x = int(input())
	endx = x % 80
	y = ends[80 - endx if endx else 0]

	if x * y > first * second:
		first = x
		second = y

	if x > ends[endx]:
		ends[endx] = x

print(first, second)