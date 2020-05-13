n = int(input())
m1 = m2 = m171 = m172 = 0
L = R = 0

for i in range(n):
    x = int(input())

    if x % 17 == 0 and x % 2 == 0 and x + m2 > L + R and m2 > 0:
        L = x; R = m2
    if x % 17 == 0 and x % 2 == 1 and x + m1 > L + R and m1 > 0:
        L = x; R = m1
    if x % 2 == 0 and x + m172 > L + R and m172 > 0:
        L = x; R = m172
    if x % 2 == 1 and x + m171 > L + R and m171 > 0:
        L = x; R = m171

    if x % 17 == 0 and x % 2 == 0 and x > m172:
        m172 = x
    elif x % 17 == 0 and x > m171:
        m171 = x
    elif x % 2 == 0 and x > m2:
        m2 = x
    elif x > m1:
        m1 = x

print(L, R)

