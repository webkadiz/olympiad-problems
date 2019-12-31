compact_number = input()

orig_number_bin = '0' * 15

for compact_digit in compact_number:

  decimal_digit = int(compact_digit, 16)

  if not decimal_digit: continue

  index = 15 - decimal_digit

  orig_number_bin = orig_number_bin[:index] + '1' + orig_number_bin[index + 1:]

orig_number_decimal = int(orig_number_bin, 2)


print(orig_number_decimal)



