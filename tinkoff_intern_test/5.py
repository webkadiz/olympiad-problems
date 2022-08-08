from bisect import bisect_left

n, q = map(int, input().split())

namesOrderMap = {}
names = []

for i in range(n):
    name = input()
    namesOrderMap[name] = i + 1
    names.append(name)

names.sort()

for i in range(q):
    k, query = input().split()
    k = int(k)

    idxLeft = bisect_left(names, query)

    candidat = names[idxLeft+k-1]

    if candidat.startswith(query):
        print(namesOrderMap[candidat])
    else:
        print(-1)
