n, m = map(int, input().split())

graph = [[0] * n for i in range(n)]

k_lights = [0] * n

for i in range(m):
  v, u = map(int, input().split())

  graph[v - 1][u - 1] = 1


for i in range(n):
  for j in range(i):
    if graph[i][j]:
      k_lights[i] += 1
      k_lights[j] += 1

for i in range(n):
  for j in range(i + 1, n):
    if graph[i][j] and graph[i][j] != graph[j][i]:
      k_lights[i] += 1
      k_lights[j] += 1

print(*k_lights)