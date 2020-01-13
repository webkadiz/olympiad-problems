a, b = map(int, input().split())


if a == b:
  print(a)
  exit()

if a == 1 or b == 1:
  print(max(a, b))
  exit()

print(2)