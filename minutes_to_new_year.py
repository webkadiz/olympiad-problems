t = int(input())

for i in range(t):
  h, m = map(int, input().split())

  m_time = 24 * 60

  m_time -= h * 60
  m_time -= m

  print(m_time)