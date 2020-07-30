n = int(input())

cur_k = 0
max_k = 0

for i in range(n):
  a, b = map(int, input().split())

  cur_k -= a
  cur_k += b

  max_k = max(cur_k, max_k)

print(max_k)


