s = input()

ksection = []

vowels = ['a', 'e', 'i', 'o', 'u', 'y']

prev = s[0]
k = 1
kall = 0


for i in range(1, len(s)):
	cur = s[i]

	if cur not in vowels and prev not in vowels:
		k += 1
	elif cur in vowels and prev in vowels:
		k += 1
	else:
		if k >= 3:
			ksection.append(k)
		k = 1

	prev = cur

if k >= 3:
	ksection.append(k)

for count in ksection:
	kall += (count - 1) // 2

print(kall)