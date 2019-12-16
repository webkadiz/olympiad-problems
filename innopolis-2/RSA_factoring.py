import math
import sys

b, k = map(int, input().split())
n = int(input(), 16)

dels = []

if k == 2:
  root = math.sqrt(n)
elif k == 4:
  root = math.sqrt(math.sqrt(n))


left = int(root // 2)
right = int(root * 2)
sqrtRight = int(math.sqrt(right))

print(left, right, sqrtRight)

kblock = 100
maxK = right // kblock

nprime = list(range(sqrtRight))
nprime[0] = nprime[1] = False

primes = []

print(sys.getsizeof(nprime) // 1024 // 1024)


for i in range(sqrtRight):
  if nprime[i]:
    for j in range(i * i, sqrtRight, i):
      nprime[j] = False

for i in range(maxK):
  start = i * kblock



nprime = list(filter(bool, nprime))

print(nprime)

d = 0

while n > 1:

  while not n % nprime[d]:
    dels.append(nprime[d])
    n //= nprime[d]

  d += 1


for num in dels:
  print(hex(num)[2:])
