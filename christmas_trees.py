n, m = map(int, input().split())
arr_x = list(map(int, input().split()))

arr_y = []

usage_coords = [*arr_x]

count = 0


while count < m:

  for tree_x in arr_x:
    
