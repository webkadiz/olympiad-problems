n = int(input())

graph = [list(map(int, input().split())) for i in range(n)]

k = 0

for i in range(n):
  for j in range(i):
    if graph[i][j]:
      k += 1

print(k)