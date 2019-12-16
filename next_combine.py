n, k = map(int, input().split())

comb = list(map(int, input().split()))
comb.sort()

for i in range(len(comb) - 1):
  if comb[i] == comb[i + 1]:
    print(-1)
    exit()

top = n
for i in range(len(comb) - 1, -1, -1):
  if comb[i] < top:
    comb[i] += 1
    if i + 1 < len(comb):
      comb[i + 1] = comb[i] + 1
    break

  top -= 1

else:
  print(-1)
  exit()



print(*comb)