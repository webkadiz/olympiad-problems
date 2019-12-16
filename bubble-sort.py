def bubble_sort(arr):
  arr = arr.copy()
  
  for i in range(len(arr)):
    for j in range(len(arr) - i - 1):
      print(arr[j], arr[j + 1])
      if arr[j] > arr[j + 1]:
        arr[j], arr[j + 1] = arr[j + 1], arr[j]

  return arr


arr = [5,4,3,2,1]
print(bubble_sort(arr))
print(arr)