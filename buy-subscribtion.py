t = int(input())




for i in range(t):
  n, k, d = map(int, input().split(' '))
  schedule = list(map(int, input().split(' ')))


  for i in range(len(schedule) - d):
    table = list([0] * (k + 1))
    for j in range(i, i + 8):
      table[schedule[j]] = 1

    amount = len(list(filter(bool, table)))
    
    print(table)
    print(amount)