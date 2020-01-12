n = int(input())
arr = list(map(int, input().split()))

def sort_insertion(arr):
  arr = arr[:]
  arr_len = len(arr)

  for i in range(1, arr_len):
    cur = arr[i]

    for j in range(i - 1, -1, -1):

      if arr[j] <= cur:
        j += 1
        break
 
      arr[j + 1] = arr[j]
    
    arr[j] = cur

  return arr

print(sort_insertion(arr))