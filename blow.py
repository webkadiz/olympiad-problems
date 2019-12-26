n = int(input())


tasks = [0] * (n if n >= 3 else 3)
tasks[0] = 0
tasks[1] = 1

for i in range(2, n):
	tasks[i] = tasks[i - 1] * 3 + (i - 1) * 2

print(3 ** n - tasks[n - 1])