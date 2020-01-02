k, n = map(int, input().split())

amount = (n - 1) // k
print(amount + 1, n % k or k)