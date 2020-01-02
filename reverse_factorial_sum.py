n = int(input())

def fac(n):
  f = [0] * (n + 2)
  f[0] = 1
  f[1] = 1

  for i in range(2, n + 1):
    f[i] = i * f[i - 1]

  return f[n]

def posting(n, k):
  res = 1
  for i in range(n, k, -1):
    res *= i

  return res




fac_n = fac(n)

fac_sum = fac_n

for i in range(1, n + 1):
  fac_sum += posting(n, i)


res = fac_sum / fac_n
print(res)
