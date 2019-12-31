n = int(input())

graph = [list(map(int, input().split())) for i in range(n)]

vertexes = set(range(n))
min_way_len = 3001
ans_vertexes = []

for i in range(n):
  for j in range(i):
    for v in range(j):
      way_len = graph[i][j] + graph[i][v] + graph[j][v]

      if way_len < min_way_len:
        min_way_len = way_len
        ans_vertexes = [i + 1, j + 1, v + 1]


print(*ans_vertexes)