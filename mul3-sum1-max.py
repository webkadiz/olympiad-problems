
m1 = m2 = m3 = 0
n = int(input())

for i in range(n):
	x = int(input())

	if not x % 2 and x > m2:
		m2 = x

	if x % 2 and x > m1:
		m1 = x

	if x % 2 and not x % 3 and x > m3:
		m3 = x

if not m2 or not (m1 or m3):
	print(0)

if m2 % 3 == 0:
	print(m2, max(m1, m3))
else:
	print(m2, m3)