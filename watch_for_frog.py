k, t = map(int, input().split())

full_ways = t // k
shift = t % k

print(abs(full_ways % 2 * k - shift))