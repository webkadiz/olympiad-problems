n = int(input())

cur = count = 1

for i in range(1, n + 1):
  print(cur, end=" ")
  count -= 1

  if not count:
    cur += 1
    count = cur

print()