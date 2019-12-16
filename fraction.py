a = int(input())
b = int(input())
c = int(input())
d = int(input())

ans = 0

def gcd(a, b):
  while b:
    a, b = b, a % b 

  return a

while a * d < c * b:
  print(a * b, c * d)
  a += 1
  b += 1
  ans += 1

  t = gcd(a, b)

  a //= t
  b //= t

if a == c and b == d:
  print(ans)
else:
  print(0) 