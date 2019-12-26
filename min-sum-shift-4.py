n = int(input())

window = [0] * 5
m = 1000
ms = 2000

for i in range(4):
	window[i] = int(input())

for i in range(4, n):
	window[4] = int(input())

	if window[0] < m: m = window[0]

	s = m + window[4]

	if s < ms: ms = s

	for j in range(4):
		window[j] = window[j + 1]

print(ms)