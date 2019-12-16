n, m = map(int, input().split())

a = [[int(s) for s in input().split()] for i in range(n)]

k = int(input())

klocal = kmax = 1
indexbest = 0

for i in range(n):
  
  for j in range(1, m):
    if not a[i][j] + a[i][j - 1]:
      klocal += 1
    else:
      klocal = 1

    if klocal > kmax:
      kmax = klocal

  if kmax >= k:
    indexbest = i + 1
    break
  
  kmax = 1
  klocal = 1

print(indexbest)
