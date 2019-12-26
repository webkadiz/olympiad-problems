length = int(input())

pairs = [int(input()) for i in range(length)]

maxSum = -1

for i in range(length):
  for j in range(i, length):
    if pairs[i] > pairs[j]:
      pairSum = pairs[i] + pairs[j]
      if pairSum % 120 == 0:
        if pairSum > maxSum:
          firstOfPair = pairs[i]
          secondOfPair = pairs[j]
          maxSum = pairSum


print(firstOfPair, secondOfPair)