n = int(input())

tasks = [0] * (n if n >=2 else 2)
tasks[0] = 3
tasks[1] = 8

for i in range(2, n):
	tasks[i] = tasks[i - 1] * 2 + tasks[i - 2] * 2

print(tasks[n - 1])