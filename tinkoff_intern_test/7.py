s = input()
n = int(input())

for i in range(n):
    l, r = map(int, input().split())

    sub = s[l-1:r]

    ssub = sorted(sub, reverse=True)

    count = 0
    idx = 0
    while True:
        letter = ssub[-1]

        if sub[idx] == letter:
            ssub.pop()

        if not ssub:
            break

        idx += 1
        count += 1

        if idx >= len(sub):
            idx = 0

    print(count)
