x1, y1 = map(int, input().split())
x2, y2 = map(int, input().split())
x3, y3 = map(int, input().split())
x4, y4 = map(int, input().split())

def inRect(x1, y1, x2, y2, x3, y3):
    return min(x1, x2) <= x3 and max(x1, x2) >= x3 and min(y1, y2) <= y3 and max(y1, y2 >= y3)

pos1 = (x3 - x1) * (y2 - y1) - (y3 - y1) * (x2 - x1)
pos2 = (x4 - x1) * (y2 - y1) - (y4 - y1) * (x2 - x1)
pos3 = (x1 - x3) * (y4 - y3) - (y1 - y3) * (x4 - x3)
pos4 = (x2 - x3) * (y4 - y3) - (y2 - y3) * (x4 - x3)

if pos1 == 0 and pos2 == 0:
    if inRect(x1, y1, x2, y2, x3, y3) or inRect(x1, y1, x2, y2, x4, y4):
        print("Yes")
    else:
        print("No")
elif pos1 * pos2 <= 0 and pos3 * pos4 <= 0:
    print("Yes")
else:
    print("No")


