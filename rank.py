k = int(input())
*arr, = map(int, input().split())
pety = int(input())


for i in range(k):
  if pety > arr[i]:
    print(i + 1)
    break
else:
  print(k + 1)