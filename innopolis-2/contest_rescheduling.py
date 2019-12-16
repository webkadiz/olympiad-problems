n = int(input())

res = []

for i in range(n):
  l1, r1, l2, r2 = map(int, input().split())
  s1, d1, s2, d2 = map(int, input().split())

  left1 = s1
  right1 = s1 + d1

  left2 = s2
  right2 = s2 + d2

  if right1 <= left2 or right2 <= left1:
    res.append([s1, s2])
  else:

    inter1 = right2 - left1
    inter2 = right1 - left2

    shift1 = inter1 // 2
    shift2 = inter2 // 2

    tleft1 = left1 + shift1
    tright1 = right2 - shift2

    tleft2 = left2 + shift1
    tright2 = right1 - shift2


    if abs(tright1 - tleft1) >= 1:
      if tright1 - 1 - d2 >= l2 and tleft1 + d1 <= r1:
        tright1 -= 1
        shift1 += 1
      elif tleft1 + d1 + 1 <= r1 and tright1 - d2 >= l2:
        tleft1 += 1
        shift1 += 1
      else:
        tleft1 = r1 + 1

    if abs(tright2 - tleft2) >= 1:
      if tright2 - d1 - 1 >= l1 and tleft2 + d2 <= r2:
        tright2 -= 1
        shift2 += 1
      elif tleft2 + d2 + 1 <= r2 and tright2 - d1 >= l1:
        tleft2 += 1
        shift2 += 1
      else:
        tleft2 = r2 + 1

      

    if not (tright1 - d2 >= l2 and tleft1 + d1 <= r1) and not (tright2 - d1 >= l1 and tleft2 + d2 <= r2):
      res.append([-1, -1])
    elif not (tright1 - d2 >= l2 and tleft1 + d1 <= r1):
      res.append([tright2 - d1, tleft2])
    elif not (tright2 - d1 >= l1 and tleft2 + d2 <= r2):
      res.append([tleft1, tright1 - d2])
    else:
      if shift2 > shift1:
        res.append([tleft1, tright1 - d2])
      else:
        res.append([tright2 - d1, tleft2])





for pair in res:
  print(*pair)