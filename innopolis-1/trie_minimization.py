n = int(input())

tree = []

kreplaces = 0

for i in range(n):
  s = input()

  for j, char in enumerate(s):
    if len(tree) == j:
      tree.append({})

    if not ~tree[j].get(char, -1):
      tree[j][char] = 1
    else:
      tree[j][char] += 1

for letter_structure in tree:
  kletters = sum(letter_structure.values())
  max_kletter = max(letter_structure.values())

  kreplaces += kletters - max_kletter

print(kreplaces)