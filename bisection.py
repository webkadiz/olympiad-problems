a = float(input())
n = int(input())


def sqrt(n, p):
    measure = n
    left = 0
    right = n

    if n < 1: right = 1
    
    eps = 1e-10

    i = 0
    while right - left > eps:
        mid = (right + left) / 2
        approx = pow(mid, p)
        
        if approx > measure:
            right = mid
        else:
            left = mid
        
        i += 1
    
    print(i)
    return right


print(sqrt(a, n))
