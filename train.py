
n = int(input())

trains = {}
prevOpers = []
printInfo = []

for i in range(n):
	inputStr = input().split()
	oper = inputStr[0]

	if oper == 'delete':
		amountDel = int(inputStr[1])

		while amountDel > 0 and prevOpers:
			name, amount = prevOpers[-1]

			if amount > amountDel:
				trains[name] -= amountDel
				prevOpers[-1][1] -= amountDel
				amountDel -= amountDel
			else:
				trains[name] -= amount
				prevOpers.pop()
				amountDel -= amount


	elif oper == 'add':
		nameAdd = inputStr[2]
		amountAdd = int(inputStr[1])

		if trains.get(nameAdd) is not None:
			trains[nameAdd] += amountAdd
		else:
			trains[nameAdd] = amountAdd

		prevOpers += [[nameAdd, amountAdd]]


	elif oper == 'get':
		nameGet = inputStr[1]
		amountGet = trains.get(nameGet, 0)
		printInfo += [amountGet]

for amount in printInfo:
	print(amount)


