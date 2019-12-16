n, k = map(int, input().split(' '))
amount = 0
arr = list(map(int, input().split(' ')))

prepare_arr = []

max_pow = 10000000001

base = 1
cpow = base ** k
while cpow < max_pow:
  prepare_arr.append(cpow)
  base += 1
  cpow = base ** k

for i in range(len(arr)):
  for j in range(i+1, len(arr)):
    mul = arr[i] * arr[j]

    if mul in prepare_arr:
      amount += 1

print(amount)