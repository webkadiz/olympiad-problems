words = input().split()


res = ''



def check(word):
	k = {}
	len_word = len(word)

	for char in word:
		if char in k:
			k[char] += 1
		else:
			k[char] = 1


	if len_word % 2:
		attempt = 1
	else:
		attempt = 0

	for amount in k.values():
		if amount % 2:
			attempt -= 1

	if attempt < 0:
		return False
	else:
		return True

for word in words:
	
	isPal = check(word)

	if isPal: continue

	res += word + ' '

print(res[:-1])