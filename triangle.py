n = int(input())



pos = [1000, 0, 0, 0, 0, 0, 0, 0, 0]
neg = [1000, 0, 0, 0, 0, 0, 0, 0, 0]

s1 = 0
s2 = 0


for i in range(n):
	x, y = map(int, input().split(' '))

	if y == 0:
		if x > 0:
			if x < pos[0]:
				pos[0] = x
				pos[1] = y
				pos[6] = 1
			elif x > pos[2]:
				pos[2] = x
				pos[3] = y
				pos[7] = 1
		elif x < 0:
			if x < neg[0]:
				neg[0] = x
				neg[1] = y
				neg[6] = 1
			elif x > neg[2]:
				neg[2] = x
				neg[3] = y
				neg[7] = 1

	elif x > 0:
		if abs(y) > abs(pos[5]):
			pos[4] = x
			pos[5] = y
			pos[8] = 1
	elif x < 0:
		if abs(y) > abs(neg[5]):
			neg[4] = x
			neg[5] = y
			neg[8] = 1


if pos[6] and pos[7] and pos[8]:
	s1 = ((pos[2] - pos[0]) * pos[5]) / 2 


if neg[6] and neg[7] and neg[8]:
	s2 = ((abs(neg[0]) - abs(neg[1])) * neg[5]) / 2 




print(max(s1, s2))