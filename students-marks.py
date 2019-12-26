n = int(input())
students  = [0] * 100


m1 = m2 = m3 = 20

for i in range(n):
	lname, name, a, b, c = input().split(' ')

	s = int(a) + int(b) + int(c)

	students[i] = {
		'lname': lname,
		'name': name,
		's': s
	}


for i in range(n):
	s = students[i]['s']

	if s < m1:
		m3 = m2
		m2 = m1
		m1 = s
	elif s < m2:
		m3 = m2
		m2 = s
	elif s < m3:
		m3 = s



for i in range(n):
	if students[i]['s'] <= m3:
		print(students[i]['lname'], students[i]['name'])

