n, k = map(int, input().split())
arr = list(map(int, input().split()))
arr_find = list(map(int, input().split()))


def bin_search(arr, el):
    left = -1
    right = len(arr)

    while right - left > 1:
        mid = (right + left) // 2

        if arr[mid] >= el:
            right = mid
        else:
            left = mid

    return left, right


for el in arr_find:
    
    left, right = bin_search(arr, el)
    print(left, right) 
    if arr[left] == el:
        print('YES')
    else:
        print('NO')


