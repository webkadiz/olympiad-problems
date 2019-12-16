n = nstep = int(input())
m = mstep = int(input())
x = int(input())

lastn = 0
lastm = 0

while 100 * n / x <= 1000:
  
  c = n * 100 / x

  if int(c) == float(c):
    c = int(c)
    m = c - n

    mIsInt = m / mstep

    if int(mIsInt) == float(mIsInt):
      lastm = m
      lastn = n

  n += nstep

print(lastn + lastm)    