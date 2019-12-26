s = input()

vowels = ['a', 'e', 'i', 'o', 'u', 'y']
consonants = []
isPal = True

for char in s:
	if char not in vowels:
		consonants.append(char)

for i in range(len(consonants) // 2):
	left = i
	right = len(consonants) - i - 1

	if consonants[left] != consonants[right]:
		isPal = False
		break


print('YES') if isPal else print('NO')
