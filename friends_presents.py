n = int(input())

graph = {}

friends = list(map(int, input().split()))
all_friends = list(range(1, n + 1))
fools = []

for i in range(len(friends)):


  graph[i + 1] = friends[i]


print(graph)

print(set(graph.values()))
print(set(graph.keys()))

ends = set(graph.values()) - set(graph.keys())

print(ends)
for k in ends:
  print(k)