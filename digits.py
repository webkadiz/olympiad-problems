*arr, = map(int, input().split())

digits = [0] * 9

for digit in arr:
  if digit:
    digits[digit - 1] += 1

print(*digits)