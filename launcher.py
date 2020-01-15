import random


sign = input()


if sign == 'Раскажи шутку':

	rand = random.randrange(3)

	jokes = ['Про лягушку', 'Мед', 'Про Васю']

	print(jokes[rand])
else:
	print('Введите корректное кодовую фразу')

