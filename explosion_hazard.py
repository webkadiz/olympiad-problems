n = int(input())
tasks = [0] * (n if n >= 2 else 2)
tasks[0] = 2
tasks[1] = 3

for i in range(2, n):
	tasks[i] = tasks[i - 1] + tasks[i - 2]

print(tasks[n - 1])
