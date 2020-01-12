def computeAmount(x1, y1, x2, y2):
  from math import gcd

  if x1 == x2 and y1 == y2:
    return 0
  elif x1 == x2:
    return abs(y2 - y1)
  elif y1 == y2:
    return abs(x2 - x1)
  else:
    diffX = abs(x2 - x1)
    diffY = abs(y2 - y1)

    return gcd(diffX, diffY)


n = int(input())

firstX, firstY = map(int, input().split())
prevX, prevY = firstX, firstY
k = 0

for i in range(n - 1):
  x, y = map(int, input().split())

  k += computeAmount(x, y, prevX, prevY)

  prevX, prevY = x, y

k += computeAmount(x, y, firstX, firstY)

print(k)