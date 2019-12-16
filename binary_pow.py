def isInt(n):
  return int(n) == float(n)

def bin_pow(num, p):
  if p == 0:
    return 1

  if p % 2:
    return num * bin_pow(num, p - 1)
  else:
    b = bin_pow(num, p // 2)
    return b * b

num = float(input())
p = int(input())


ans = bin_pow(num, p)

print(ans)