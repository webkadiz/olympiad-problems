da, db = map(int, input().split(' '))

if db - da == 0:
  print(da * 10, db * 10 + 1)
elif db - da == 1:
  print(da * 10 + 9, db * 10)
elif da == 9 and db == 1:
  print(99, 100)
else:
  print(-1)