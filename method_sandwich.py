s = list(input())
s.pop()

sans = []

for i, char in enumerate(s):
	if (i + 1) % 2:
		sans.insert( len(sans) // 2,char)
	else:
		sans.insert( (len(sans) + 1) // 2,char)

print(''.join(sans))