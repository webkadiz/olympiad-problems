n_orig = int(input())

n = abs(n_orig)

table = ['$', '0', '1']

if n < 2:
  print(table[n_orig + 1])
  exit()

hold = 2
p = 1

while hold + 3 ** p <= n:
  hold += 3 ** p
  p += 1


new = n - hold
ans = ''

for i in range(p):
  ldigit = new % 3
  ans = table[ldigit] + ans
  new //= 3

ans = '1' + ans


if n_orig < 0:
  for char in ans:
    if char == '$':
      print('1', sep='', end='')
    elif char == '1':
      print('$', sep='', end='')
    else:
      print('0', sep='', end='')

else:
  print(ans)