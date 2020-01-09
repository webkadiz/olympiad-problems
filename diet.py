x, y, z = map(float, input().split())
n = int(input())

kx = ky = kz = 0

exp = 1e-10

for i in range(n):
  x0, y0, z0, k = map(float, input().split())

  kx += x0 * k
  ky += y0 * k
  kz += z0 * k



if kx >= x - exp and ky >= y - exp and kz >= z - exp:
  print('YES')
else:
  print('NO')
