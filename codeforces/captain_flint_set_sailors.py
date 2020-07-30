t = int(input())
ans = []
almost_simple = [6, 10, 14, 15]

for i in range(t):
  n = int(input())

  res_almost_simple = [6, 10, 14]

  four = n - sum(res_almost_simple) # four add
  if four in res_almost_simple:
    res_almost_simple[2] = 15
  four = n - sum(res_almost_simple)

  if four > 0:
    ans.append(["YES", [*res_almost_simple, four]])
  else:
    ans.append(["NO"])

for item in ans:
  print(item[0])
  if item[0] == "YES":
    print(*item[1])



