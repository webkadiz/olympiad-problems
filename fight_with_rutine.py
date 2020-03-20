n = int(input())

types = list(map(int, input().split()))

res = [0] * n

for i in range(n):

    keys = set()
    for j in range(i, -1, -1):
        keys.add(types[j])
        
        res[i - j] += len(keys)


print(*res)
