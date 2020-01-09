
m = count = 0

x = int(input())
while x:

  if x == m:
    count += 1

  if x > m:
    m = x
    count = 1


  x = int(input())

print(count)