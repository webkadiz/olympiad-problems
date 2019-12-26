a, b = map(int, input().split(' '))
x, y = map(int, input().split(' '))


s, v = x, y
k = 0

def gcd(a,b):
	while b:
		a, b = b, a % b

	return a


while gcd(s, v) != 1:
	d = gcd(s, v)
	s /= d
	v /= d
	
	if s <= a and v <= b: 
		k += 1


s, v = x, y
mul = 2
while s <= a and v <= b:
	s, v = x, y
	s *= mul
	v *= mul

	k += 1
	mul += 1


print(k)