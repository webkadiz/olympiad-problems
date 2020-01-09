x, y = map(float, input().split())

exp = 0.0001

count = 1
while y - x > exp:
  
  x += x * 0.7
  count += 1

print(count)