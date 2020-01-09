n = int(input())

graph = [list(map(int, input().split())) for i in range(n)]

k_sources = k_stocks = 0
sources = []
stocks = []

for i in range(n):
  for j in range(n):
    if graph[j][i]: break
  else:
    k_sources += 1
    sources += [i + 1]
    
    
  for j in range(n):
    if graph[i][j]: break
  else:
    k_stocks += 1
    stocks += [i + 1]

sources.sort()
stocks.sort()

print(k_sources)
print(*sources, sep="\n")
print(k_stocks)
print(*stocks, sep="\n")