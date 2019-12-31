n, m = map(int, input().split())



graph = [[0] * n for i in range(n)]

for i in range(m):
  u, v = map(int, input().split())

  graph[u - 1][v - 1] = 1
  graph[v - 1][u - 1] = 1

isTrans = True

if m <= 1:
  print('Yes')
  exit()

# for i in range(n):
#   for j in range(n):
#     if graph[i][j]:
#       for t in range(n):
#         if t == i or t == j: continue
#         if graph[j][t]:
#           if not graph[i][t] and not graph[t][i]:
#             isTrans = False

for i in range(n):
  for j in range(i):
    for t in range(j):
      if graph[i][j] and graph[j][t]:
        if not graph[i][t] and not graph[t][i]:
          isTrans = False


print('YES' if isTrans else 'NO')