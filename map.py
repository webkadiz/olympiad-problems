n, k = map(int, input().split())

graph = []
printInfo = []

for i in range(n):
	graph.append([])



for i in range(k):
	oper, u, v = input().split()
	u = int(u) - 1
	v = int(v) - 1

	if oper == '+':
		graph[u] += [v]
		graph[v] += [u]

	if oper == '?':

		if not(graph[u] and graph[v]):
			printInfo += ['?']
		elif set(graph[u]) & set(graph[v]):
			printInfo += ['+']
		else:
			printInfo += ['-']

for info in printInfo:
	print(info)