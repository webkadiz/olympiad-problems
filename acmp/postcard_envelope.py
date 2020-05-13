from math import cos, sin, pi

card_w, card_h = map(int, input().split())
env_w, env_h = map(int, input().split())


eps = 1e-10

if card_w == env_h and card_h == env_w:
    print('Possible')
    exit()
    

def check_insert(w, h):
    if w <= env_w + eps and h <= env_h + eps:
        return True
    else:
        return False

def rotate_on_degree(deg):
    rad = pi * deg / 180
    w = cos(rad) * card_w + sin(rad) * card_h
    h = sin(rad) * card_w + cos(rad) * card_h

    return w, h


i = 0
while i < 90:
    w, h = rotate_on_degree(i)
    res = check_insert(w, h)
    
    if res:
        print('Possible')
        exit()
    
    i += 0.0005
print('Impossible')


