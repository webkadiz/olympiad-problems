x1, y1 = map(int, input().split())
x2, y2 = map(int, input().split())
x3, y3 = map(int, input().split())
x4, y4 = map(int, input().split())


def pos(x1, y1, x2, y2, x3, y3):
    return (x2 - x1) * (y3 - y1) - (x3 - x1) * (y2 - y1)

cond1 = pos(x1, y1, x2, y2, x3, y3) * pos(x1, y1, x2, y2, x4, y4)
cond2 = pos(x2, y2, x3, y3, x1, y1) * pos(x2, y2, x3, y3, x4, y4)
cond3 = pos(x1, y1, x3, y3, x2, y2) * pos(x1, y1, x3, y3, x4, y4)

if cond1 >= 0 and cond2 >= 0 and cond3 >= 0:
    print("In")
else:
    print("Out")


