import re

crypt = input()

decrypt = re.sub('[0-9]+', '', crypt)

i = 1
j = 1
while i + 1 < len(crypt):

  if 48 <= ord(crypt[i + 1]) <= 57:
    shift_str = ''

    while i + 1 < len(crypt) and 48 <= ord(crypt[i + 1]) <= 57:
      shift_str += crypt[i + 1]
      i += 1

    shift = int(shift_str)

    letter_idx = j
    letter = decrypt[letter_idx]

    decrypt = decrypt[:letter_idx] + decrypt[letter_idx + 1:]

    new_letter_idx = (letter_idx + shift) % len(decrypt)

    decrypt = decrypt[:new_letter_idx] + letter + decrypt[new_letter_idx:]

  j += 1
  i += 1


print(decrypt)

