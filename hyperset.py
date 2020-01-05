n, k = map(int, input().split())

cards = [input() for i in range(n)]
count = 0

def isSet(a, b, c):

  for i in range(k):
    if not(a[i] == b[i] and b[i] == c[i] or a[i] != b[i] and a[i] != c[i] and b[i] != c[i]):
      return False

  return True

for i in range(n):
  for j in range(i + 1, n):
    for t in range(j + 1, n):
      if isSet(cards[i], cards[j], cards[t]):
        count += 1

print(count)