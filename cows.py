n_str = input()
n = int(n_str)

if 1 <= n - 10 <= 4:
  print(n_str + ' korov')
elif n % 10 == 1:
  print(n_str + ' korova')
elif 2 <= n % 10 <= 4:
  print(n_str + ' korovy')
else:
  print(n_str + ' korov')