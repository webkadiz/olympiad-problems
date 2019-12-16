n, k = map(int, input().split())

a = list(map(int, input().split()))

sum_ends = 0

for i in range(n):
  if i % 2 and i == (n - 1):
    left = n
    clen = sum_ends

  if i % 2: continue

  left = i
  right = len(a) - i - 1

  clen = a[right] - a[left] + sum_ends
 
  sum_ends += (a[left + 1] - a[left]) + (a[right] - a[right - 1])

  if clen <= k:
    break

print(clen, k)

if clen != k:
  print('No')
else:
  print('Yes')
  
  for i in range(n):
    if i < left:
      if i % 2: continue
      print(i + 1, i + 2)
      print(len(a) - i - 1, len(a) - i)
    else:
      print(left + 1, right + 1)
      
      left += 1
      right -= 1


