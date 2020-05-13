n = int(input())

sqrtN = int(n ** 0.5)
muls= [0] * (sqrtN+1)
ans=''


d = 2
while d <= sqrtN:
    
    while n % d == 0:
        muls[d] += 1
        n //= d

    d += 1

for i in range(2, sqrtN+1):
    for j in range(muls[i]):
        ans += str(i) + '*'

if n == 1:
    print(ans[:-1])
else:
    print(ans + str(n))

