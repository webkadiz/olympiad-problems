n, m, k = map(int, input().split())

if k <= 2:
  print(0)
  exit()

b_kids = (n - 1) // (k - 2) + 1
rest_kids = b_kids * (k - 2) - n
m_need = b_kids * 2

if m_need > m:
  print(0)
elif m - m_need <= rest_kids:
  print(b_kids)

else:
  m_rest = m - m_need - rest_kids

  print(b_kids + ((m_rest - 1) // k + 1))


