beg, end = map(int, input().split())

if end < 1605:
  print(0)
elif beg < 1605:
  rang = end - 1605

  print(rang // 10 + 1)
else:
  rang = end - beg
  ans = rang // 10 + 1

  
  if beg % 5 == 0:
    ans -= 1

  print(ans)
