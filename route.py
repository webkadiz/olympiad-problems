from math import inf

n = int(input())

cost = [list(map(int, list(input()))) for i in range(n)]
dp = [[0] * n for i in range(n)]
dp[0][0] = cost[0][0]

for i in range(1, n):
    dp[0][i] = dp[0][i-1] + cost[0][i]
    dp[i][0] = dp[i-1][0] + cost[i][0]

for i in range(1, n):
    for j in range(1, n):
        dp[i][j] = min(dp[i][j-1], dp[i-1][j]) + cost[i][j] 

for i in range(n):
    for j in range(n):
        cost[i][j] = '-'

k = n - 1
m = n - 1
cost[k][m] = '#'
while k or m:
        
    up = inf if k-1 < 0 else dp[k-1][m]
    left = inf if m-1 < 0 else dp[k][m-1]

    if up < left:
        cost[k-1][m] = '#'
        k -= 1
    else:
        cost[k][m-1] = '#'
        m -= 1
    
for i in range(n):
    for j in range(n):
        print(cost[i][j], sep='', end='')
    print()
