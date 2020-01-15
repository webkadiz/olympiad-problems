n = int(input())
cost = list(map(int, input().split()))



tasks = [0] * n
tasks[0] = cost[0]

if n > 1: tasks[1] = cost[1]

for i in range(2, n):
	tasks[i] = min(tasks[i - 1], tasks[i - 2]) + cost[i]

print(tasks[n - 1])