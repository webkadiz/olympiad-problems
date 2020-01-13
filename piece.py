from math import gcd

a, b, c, d = map(int, input().split())

x = abs(a - c)
y = abs(b - d)

if not y or not x:
  print(0)
  exit()

nod = gcd(x, y)

print((x // nod + y // nod - 1) * nod)