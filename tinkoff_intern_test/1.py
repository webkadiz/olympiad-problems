x1, y1, x2, y2 = list(map(int, input().split()))
x3, y3, x4, y4 = list(map(int, input().split()))

minX = min(x1, x2, x3, x4)
minY = min(y1, y2, y3, y4)
maxX = max(x1, x2, x3, x4)
maxY = max(y1, y2, y3, y4)

disX = maxX - minX
disY = maxY - minY

disMax = max(disX, disY)

print(disMax * disMax)
