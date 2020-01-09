def intersection(ax1, ay1, ax2, ay2, bx1, by1, bx2, by2):
  v1 = (bx2 - bx1) * (ay1 - by1) - (by2 - by1) * (ax1 - bx1)
  v2 = (bx2 - bx1) * (ay2 - by1) - (by2 - by1) * (ax2 - bx1)
  v3 = (ax2 - ax1) * (by1 - ay1) - (ay2 - ay1) * (bx1 - ax1)
  v4 = (ax2 - ax1) * (by2 - ay1) - (ay2 - ay1) * (bx2 - ax1)
  
  return v1 * v2 < 0 and v3 * v4 < 0


k = int(input())

k_intersect = 0

prevX = prevY = None
lines = []

for i in range(k):
  x, y = map(int, input().split())

  if prevX != None:
    line = [prevX, prevY, x, y]

    for other_line in lines:

      isIntersection = intersection(*line, *other_line)

      if isIntersection:
        k_intersect += 1

    lines.append(line)

  prevX = x
  prevY = y


print(k_intersect)

  
