n = int(input())

tasks = [0] * (n if n >= 3 else 3)
tasks[0] = 2
tasks[1] = 4
tasks[2] = 7


for i in range(3, n):
	tasks[i] = tasks[i - 1] + tasks[i - 2] + tasks[i - 3]

print(tasks[n - 1])
