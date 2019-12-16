n = int(input())

numbers = list(map(int, input().split()))

ms = 0
m = 10000
search = -1

for j in range(n - 2):

  for i in range(1, len(numbers) - 1):
    p = p1 = p2 = p3 = 0
    p1 = (numbers[i - 1] + numbers[i + 1]) * numbers[i]
    if i - 2 >= 0:
      p2 = (numbers[i - 2] + numbers[i + 1]) * numbers[i - 1]

    if i + 2 < len(numbers):
      p3 = (numbers[i + 2] + numbers[i - 1]) * numbers[i + 1]
    p = p1 + p2 + p3

    if p < m:
      m = p1
      search = i


  numbers.pop(search)
  ms += m
  m = 10000

print(ms)