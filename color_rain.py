n = int(input())

graph = [list(map(int, input().split())) for i in range(n)]
input()
*colors, = map(int, input().split())

k = 0

for i in range(n):
  for j in range(i):
    if graph[i][j] and colors[i] != colors[j]:
      k += 1


print(k)