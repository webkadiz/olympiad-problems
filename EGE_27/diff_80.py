n = int(input())
mem = [[0, 0] for i in range(80)]
m1 = m2 = 0
m = 80

for i in range(n):
	x = int(input())
	p = x % m
	y_min = mem[p][0]
	y_max = mem[p][1]

	if y_max and abs(x - y_max) > abs(m1 - m2):
		m1 = x
		m2 = y_max

	if y_min and abs(x - y_min) > abs(m1 - m2):
		m1 = x
		m2 = y_min

	if x < y_min or not y_min:
		mem[p][0] = x

	if x > y_max:
		mem[p][1] = x


print(m1, m2)