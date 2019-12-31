def isColSafe(col):
  return 0 <= col < m

def isRowSafe(row):
  return 0 <= row < n

def isDiffOne(next, cur):
  return next - 1 == cur

def build_snake(row, col, amount):
  nextAmount = amount + 1
  cur = matrix[row][col]
  colLeft = col - 1
  colRight = col + 1
  rowUp = row - 1
  rowDown = row + 1

  if isColSafe(colLeft) and isDiffOne(matrix[row][colLeft], cur):
    build_snake(row, colLeft, nextAmount)

  if isColSafe(colRight) and isDiffOne(matrix[row][colRight], cur):
    build_snake(row, colRight, nextAmount)

  if isRowSafe(rowUp) and isDiffOne(matrix[rowUp][col], cur):
    build_snake(rowUp, col, nextAmount)

  if isRowSafe(rowDown) and isDiffOne(matrix[rowDown][col], cur):
    build_snake(rowDown, col, nextAmount)

  arr_amount.append(amount)
  
 
n, m = map(int, input().split())

matrix = [list(map(int, input().split())) for i in range(n)]

arr_amount = []

for i in range(n):
  for j in range(m):
    build_snake(i, j, 1)


print(max(arr_amount))