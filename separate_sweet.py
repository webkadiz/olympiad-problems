t = int(input())

for i in range(t):
  n, k = map(int, input().split())

  if int(n / k) == float(n / k):
    print(n)
    continue

  a = n // k

  m_k = k // 2

  ans = k * a + m_k

  if ans > n:
    print(n)
  else:
    print(ans)