def compute_time(increase):
    time = 0

    for i in range(n):
        time += length[i] / (speed[i] + increase)
    
    return time


def bin_search(arr, el):
    left = -1
    right = len(arr)

    while right - left > 1:
        mid = (right + left) // 2

        if arr[mid] >= el:
            right = mid
        else:
            left = mid

    return left


def increase_search(diff_time):
    left = 0
    right = 10 ** 9

    while right - left > 1:
        mid = (right + left) // 2
        time = compute_time(mid)
        print(left, right)        
        if time <= diff_time:
            right = mid
        else:
            left = mid

    return right



n = int(input())
speed = list(map(int, input().split()))
length = list(map(int, input().split()))
m = int(input())
border = list(map(int, input().split()))
fol = list(map(int, input().split()))
q = int(input())

ans = [0] * n

time = [0] * n
border_time = 0
for i in range(n):
    t_time = length[i] // speed[i]
    time[i] = t_time
    border_time += t_time


for i in range(q):
    s, t = map(int, input().split())
    diff_time = t - s

    if diff_time >= border_time:
        ans[i] = 0
    else:
        increase = increase_search(diff_time)
                
        idx = bin_search(border, increase)
        
        cur_fol = fol[idx + 1]

        ans[i] = cur_fol

print(*ans, sep="\n")

