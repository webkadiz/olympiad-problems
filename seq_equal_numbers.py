
m_count = 1
count = 1
prev = 0

x = int(input())
while x:

  if prev == x:
    count += 1
    if count > m_count:
      m_count = count
  else:
    count = 1

  prev = x
  x = int(input())

print(m_count)