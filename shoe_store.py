size_leg = int(input())
n = int(input())

sizes = sorted(list(map(int, input().split())))

able = size_leg
k = 0

for size in sizes:
  if size < size_leg: continue

  if size >= able:
    able = size + 3
    k += 1

print(k)