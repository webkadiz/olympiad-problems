a = input()
b = input()
c = input()
d = input()

kF = kS = 0

lenF = min(len(a), len(c))
lenS = min(len(b), len(d))

for i in range(lenF):
	if a[-1 - i] != c[-1 - i]:
		break

	kF += 1

for i in range(lenS):
	if b[-1 - i] != d[-1 - i]:
		break

	kS += 1

print(max(kF, kS))


