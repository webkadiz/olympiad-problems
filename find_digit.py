n = input()

m_diff = -1
m_number = -1

for i in range(len(n)):
  number = len(n) - i
  digit = int(n[i])

  if abs(digit - number) > m_diff:
    m_diff = abs(digit - number)
    m_number = number

print(m_number)




