n = int(input())

subtasks = [0] * (n if n > 3 else 3)
subtasks[0] = 1
subtasks[1] = 2
subtasks[2] = 4

for i in range(3, n):
	subtasks[i] = subtasks[i - 1] + subtasks[i - 2] + subtasks[i - 3]

print(subtasks[n - 1])