n, m = map(int, input().split())

domains = []

for i in range(n):
    domain = input()
    domains.append(domain)

for i in range(m):
    p, q = input().split()

    count = 0

    for domain in domains:
        if domain.startswith(p) and domain.endswith(q):
            count += 1

    print(count)
