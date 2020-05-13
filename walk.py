

def move_to_left():
    global a, b, c, d, x, y, x1, x2, y1, y2
    
    if a == 0:
        return True
    else:
        r = x - x1
        whole, rest = r // a, r % a

        if whole:
            x = x1 + rest
            return True
        else:
            return False

def move_to_right():
    global a, b, c, d, x, y, x1, x2, y1, y2

    if b == 0:
        return True
    else:
        r = x2 - x
        whole, rest = r // b, r % b

        if whole:
            x = x2 - rest
            return True
        else:
            return False


def move_to_bottom():
    global a, b, c, d, x, y, x1, x2, y1, y2
    
    if c == 0:
        return True
    else:
        r = y - y1
        whole, rest = r // c, r % c

        if whole:
            y = y1 + rest
            return True
        else:
            return False



def move_to_up():
    global a, b, c, d, x, y, x1, x2, y1, y2
    
    if d == 0:
        return True
    else:
        r = y2 - y
        whole, rest = r // d, r % d

        if whole:
            y = y2 - rest
            return True
        else:
            return False

t = int(input())
ans = []


for i in range(t):

    a, b, c, d = map(int, input().split())
    x, y, x1, y1, x2, y2 = map(int, input().split())

    hor = False
    vert = False

    if move_to_left():
        hor = move_to_right()
    else:
        if move_to_right():
            hor = move_to_left()

    if move_to_up():
        vert = move_to_bottom()
    else:
        if move_to_bottom():
            vert = move_to_up()

    if hor and vert:
        ans.append('Yes')
    else:
        ans.append('No')


print(*ans, sep='\n')
