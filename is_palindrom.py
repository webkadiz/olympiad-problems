s = input()

snorm = ''.join(s.split())

for i in range((len(snorm) + 1) // 2):
  left = i
  right = len(snorm) - i - 1
  
  if snorm[left] != snorm[right]:
    break
else:
  print('yes')
  exit()

print('no')