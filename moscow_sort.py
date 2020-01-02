n = int(input())
*arr, = map(int, input().split())

k = 0

def bubble_sort(arr):
  arr_local = arr[:]
  l = len(arr)

  for i in range(l):
    for j in range(i + 1, l):
      if arr_local[i] > arr_local[j]:
        arr_local[j], arr_local[i] = arr_local[i], arr_local[j]


  return arr_local

arr_sort = bubble_sort(arr)

for el1, el2 in zip(arr, arr_sort):
  if el1 != el2:
    k += 1

print(k)
 