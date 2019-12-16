bs = '92 9e 87 96 92 8a 92 df 8c 9a 9c 8a 8d 96 8b 86'.split(' ')

for byte in bs:
  print(bin(int('0x' + byte, 16)))