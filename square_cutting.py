a, b = map(int, input().split())

k = 0
while a and b:
  if a > b:
    k += a // b
    a = a % b
  else:
    k += b // a
    b = b % a 

print(k)