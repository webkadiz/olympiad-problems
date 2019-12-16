

import math

kpeople = int(input())

root = math.ceil(math.sqrt(kpeople))

ends = []

print(root)

for i in range(2, root + 1):
  print(kpeople, i)
  while not kpeople % i:
    ends.append(i)
    kpeople /= i

print(kpeople)
print(ends)