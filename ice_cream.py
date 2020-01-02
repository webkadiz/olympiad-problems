k = int(input())

if k == 1 or k == 2 or k == 4 or k == 7:
  print('NO')
  exit()




if k % 5 == 1 and k // 5 % 2:
  print('NO')
else:
  print('YES')