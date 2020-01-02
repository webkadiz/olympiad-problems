a = float(input())
b = float(input())
c = float(input())

exp = 1e-10

if abs(a + b - c) < exp:
  print('YES')
else:
  print('NO')