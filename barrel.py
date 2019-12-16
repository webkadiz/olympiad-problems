volume, volume_rest, k_buckets = map(int, input().split())

buckets = list(map(int, input().split()))

v = volume - volume_rest

tasks = [[0] * v for i in range(len(buckets))]

for i in range(len(tasks)):

  for j in range(len(tasks[i])):
    prev = tasks[i - 1][j] if i - 1 >= 0 else 0
    weight = buckets[i] if j + 1- buckets[i] >= 0 else 0

    if weight:
      rest = tasks[i-1][j-weight] if j - weight >= 0 and i - 1 >= 0 else 0
    else:
      rest = 0

    tasks[i][j] = max(prev, weight + rest)

print(tasks)