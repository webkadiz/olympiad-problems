n = int(input())

doubleMap = {}
graph = {}
chain = 0

for i in range(n):
    s, f = map(int, input().split())

    if s == f:
        doubleMap.setdefault(s, 0)
        doubleMap[s] += 1
        continue

    graph.setdefault(s, f)

    if f < graph.get(s, -1):
        graph[s] = f

cur = min(graph.keys())
while graph.get(cur) != None:
    chain += doubleMap.get(cur, 0)
    chain += 1

    cur = graph.get(cur)

print(chain)
