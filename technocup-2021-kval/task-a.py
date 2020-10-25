import math


t = int(input())

all_ans = []

for j in range(t):

    n = int(input())
    n_prints = [int(i) for i in input().split()]

    ans = []

    for i in range(n//2):
        a1 = n_prints[i*2]
        a2 = n_prints[i*2+1]
        common = abs(a1 * a2) // math.gcd(a1, a2)
        b1 = abs(common // a1)
        b2 = abs(common // a2)

        if a1*b1 + a2*b2 != 0:
            b1 *= -1

        ans.extend([b1, b2])

    all_ans.append(ans)


[print(*ans) for ans in all_ans]