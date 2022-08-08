n = int(input())

nums = list(map(int, input().split()))

subMin = float('inf')
subMinIdx = -1
unsubMax = 0
unsubMaxIdx = -1

for i in range(n):
    if i % 2 == 0 and nums[i] < subMin:
        subMin = nums[i]
        subMinIdx = i
    if i % 2 == 1 and nums[i] > unsubMax:
        unsubMax = nums[i]
        unsubMaxIdx = i

if subMin < unsubMax:
    nums[subMinIdx], nums[unsubMaxIdx] = nums[unsubMaxIdx], nums[subMinIdx]

subSum = 0
unsubSum = 0

for i in range(n):
    if i % 2 == 0:
        subSum += nums[i]
    else:
        unsubSum += nums[i]

print(subSum - unsubSum)
