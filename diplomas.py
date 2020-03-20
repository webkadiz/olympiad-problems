
w, h, n = map(int, input().split())

def k_fit_dip(side):
    w_k = side // w
    h_k = side // h

    return w_k * h_k

def size_search():
    left = 0
    right = 10 ** 14

    while right - left > 1:
        mid = (right + left) // 2
        k_dip = k_fit_dip(mid)
        
        if k_dip >= n:
            right = mid
        else:
            left = mid

    return right


print(size_search())



