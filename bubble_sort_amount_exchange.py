n = int(input())
*arr, = map(int, input().split())

def bubble_sort(arr):
  arr = arr[:]
  arr_len = len(arr)

  k = 0

  for i in range(arr_len):
    for j in range(1, arr_len - i):
      if arr[j - 1] > arr[j]:
        arr[j - 1], arr[j] = arr[j], arr[j - 1]
        k += 1
  
  return k


print(bubble_sort(arr))
