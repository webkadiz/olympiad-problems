n = int(input())
arr = list(map(int, input().split()))

def choose_max_sort(arr):
  arr = arr[:]
  arr_len = len(arr)

  for amount_sort in range(arr_len):
    cur_index_max = 0
    for j in range(arr_len - amount_sort):
      if arr[j] > arr[cur_index_max]:
        cur_index_max = j

    max_el = arr[cur_index_max]

    for k in range(cur_index_max, arr_len - amount_sort - 1):
      arr[k] = arr[k + 1]

    arr[arr_len - amount_sort - 1] = max_el

  return arr


print(*choose_max_sort(arr))