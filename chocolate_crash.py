n = int(input())
m = int(input())
k = int(input())

choc = n * m
choc_crash = choc - k

if k > choc:
  print('NO')
  exit()
  
if choc_crash % n == 0 or choc_crash % m == 0:
  print("YES")
else:
  print('NO')