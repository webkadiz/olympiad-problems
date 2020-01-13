arr = [3, 4, 8, 5, 9, 11, 7, 1, 2]

def sort_shell(arr):
  arr = arr[:]
  inc = len(arr) // 2

  while inc:
    for i, el in enumerate(arr):
      while i >= inc and arr[i - inc] > el:
          arr[i] = arr[i - inc]
          i -= inc
      arr[i] = el

    inc = 1 if inc == 2 else int(inc * 5.0 / 11)

  return arr


print(sort_shell(arr))