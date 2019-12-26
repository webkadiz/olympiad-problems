n = int(input())

stasks = [0] * (2 * n + 2)
stasks[0] = 0
stasks[1] = 1




for i in range(2, (2 * n + 2), 2):
	t = (i - 2) // 2

	stasks[i] = stasks[i // 2] + 1
	
	if t > 0:
		stasks[i - 1] = stasks[i] + stasks[t]



print(stasks[n])