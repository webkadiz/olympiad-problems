a, b, c = map(int, input().split())

c = str(c)

right = str(a // b)

index = 1
for i in range(len(c) - 1, -1, -1):
  if c[i] != right[i]:
    print(index)
    break

  index += 1