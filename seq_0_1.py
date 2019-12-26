n = int(input())

tasks = [0] * (n + 1 if n + 1 >= 3 else 3)
tasks[0] = 1
tasks[1] = 2

for i in range(2, n + 1):
	tasks[i] =  tasks[i - 1] + tasks[i - 2]

print(tasks[n])