import math

n = int(input())

if n == 1:
  print(1)
  print(1)
  exit()

mk = k = 2
number = n

step = 2


while step < n:

  for j in range(2, i):
    if i % j == 0:
      k += 1

  if k > mk:
    mk = k
    number = i

  k = 2
  step *= 2

print(number)
print(mk)


