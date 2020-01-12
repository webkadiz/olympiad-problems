def normalizeWord(word):
  s = ''
  sign = ['.', '!', ',', '?', ':', '-', ';', '(', ')']
  for char in word:
    if char in sign: continue
    s += char

  return s

output = open('output.txt', 'w', encoding='cp866')

for line in open('input.txt', 'r', encoding='cp866'):
  lineNormalized = line.strip()

  words = lineNormalized.split()
  wordsNormalized = map(normalizeWord, words)
  wordsFilter = filter(bool, wordsNormalized)
  wordsFilterLen = 0
  amountWrongWords = 0  

  for word in wordsFilter:
    letters = set(word)

    if len(letters) <= 3:
      amountWrongWords += 1

    wordsFilterLen += 1

  if amountWrongWords < (wordsFilterLen + 1) // 2:
    output.write(line)

output.close()