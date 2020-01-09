a, b, c = map(int, input().split())

def isInt(n):
  return int(n) == float(n)

if c >= 0:
  if a == 0 and c * c - b == 0:
    print('MANY SOLUTIONS')
  elif a == 0 and c * c - b:
    print('NO SOLUTION')
  else:
    res = (c * c - b) / a

    if isInt(res):
      print(int(res))
    else:
      print('NO SOLUTION')
else:
  print('NO SOLUTION')