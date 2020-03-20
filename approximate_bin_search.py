
n, k = map(int, input().split())
arr = list(map(int, input().split()))
arr_serve = list(map(int, input().split()))


def bin_search(arr, el):
    left = -1
    right = len(arr)
    
    while right - left > 1:
        mid = (right + left) // 2

        if arr[mid] > el:
            right = mid
        else:
            left = mid

    if left == -1:
        return arr[right]
    elif right == len(arr):
        return arr[left]
    elif el - arr[left] <= arr[right] - el:
        return arr[left]
    else:
        return arr[right]
        

for el in arr_serve:

    print(bin_search(arr, el))



