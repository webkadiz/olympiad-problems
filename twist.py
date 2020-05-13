n = int(input())

start = 1
end = n ** 2

table = [[0] * n for i in range(n)]

i = 0
j = 0
k = 0
while start <= end:

    for j in range(k, n-k):
        table[i][j] = start
        start += 1
    
    for i in range(k+1, n-k):
        table[i][j] = start
        start += 1
    
    for j in range(n-2-k, k-1, -1):
        table[i][j] = start
        start += 1
    
    for i in range(n-2-k, k, -1):
        table[i][j] = start
        start += 1
    
    k += 1

[print(*table[i]) for i in range(n)]


