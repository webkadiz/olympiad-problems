n = int(input())

res = 1

f = 1
for i in range(1, n + 1):
  f *= i

  res += 1 / f

print(res)