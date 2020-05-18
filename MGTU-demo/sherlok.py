words = input().split()
res = ''


fib = [0, 1, 1, 2, 3, 5, 13, 89, 233]


for word in words:
	len_word = len(word)

	res += word
	res += ' '

	if len_word in fib:
		res += word
		res += ' '




print(res)
