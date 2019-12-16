n = int(input())
print(sum(range(1, n + 1)) - sum([int(input()) for i in range(n - 1)]))