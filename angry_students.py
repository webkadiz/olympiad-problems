t = int(input())

ans = []

def isElseGame(s):
  for i in range(len(s) - 1):
    if s[i] == 'A' and s[i + 1] == 'P':
      return True

  return False

for i in range(t):
  k = int(input())
  s = input()
  count = 0

  while isElseGame(s):
    old_s = list(s)
    new_s = list(s)

    for i in range(len(old_s) - 1):
      if old_s[i] == 'A' and old_s[i + 1] == 'P':
        new_s[i + 1] = 'A'

    s = ''.join(new_s)
    count += 1


  ans.append(count)

print(*ans, sep="\n")
