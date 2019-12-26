n = int(input())

a = int(input())
b = int(input())
c = int(input())

timeBestLocal = 0
timeBestAll = 0

for i in range(n, (n + 1) // 2, -1):
	timeN = i * c + (n - i) * a
	timeLift = i * c
	timeBelow = 0

	for j in range((i + 1) // 2, 0, -1):
		t = min((i - j) * b + timeLift, j * a)

		if timeBelow and t < timeBelow: break

		timeBelow = t

	timeBestLocal = max(timeBelow, timeN)

	if timeBestAll and timeBestLocal > timeBestAll: break

	timeBestAll = timeBestLocal

if n == 1:
	print(c if a > c else a)
	exit()

print(timeBestAll)