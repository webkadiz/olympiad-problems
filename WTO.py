from math import gcd

a, b, c = map(int, input().split())
 



nod = gcd(a, b)
cut_k = (a // nod + b // nod - 1) * nod

fill_k = (a * b - cut_k) // 2

if fill_k // c:
  if not fill_k % c:
    print(0)
    exit()

print(c - fill_k % c)
