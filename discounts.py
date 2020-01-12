n = int(input())
*arr, = map(int, input().split())

s = 0
for i, el in enumerate(sorted(arr, reverse=True)):
  if i % 3 == 2: continue
  s += el

print(s)