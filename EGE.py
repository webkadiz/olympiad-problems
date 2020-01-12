eq = input()

i = 0
while i < len(eq):

  if 48 <= ord(eq[i]) <= 57:
    dig = eq[i]

    while i + 1 < len(eq) and 48 <= ord(eq[i + 1]) <= 57:
      dig += eq[i + 1]
      i += 1

    int_dig = int(dig)

    if int_dig > 5:
      print('NO')
      exit()

  i += 1


print('YES')