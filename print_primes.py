import math

m, n = map(int, input().split())

sqrtN = int(math.sqrt(n))

primes = [True] * (n + 1)
primes[0] = primes[1] = False

for i in range(3, sqrtN + 1, 2):
  if primes[i]:
    for j in range(i*i, n + 1, i):
      primes[j] = False



real_primes = [2]

if m <= 2:
  real_primes.append(2)

start = m if m % 2 else m + 1
start = start if start > 2 else 3
print(start)
for i in range(start, n + 1, 2):

  if primes[i]:
    real_primes.append(i)


# import math

# m, n = map(int, input().split())

# primes = []

# for i in range(m, n + 1):

#   sqrtI = int(math.sqrt(i)) + 1

#   isPrime = True

#   for j in range(2, sqrtI):
#     if not i % j:
#       isPrime = False
#       break

#   if isPrime:
#     primes.append(i)

# print(primes)


# m, n = map(int, input().split())

# primes = [2]


# for i in range(3, n + 1, 2):
#   j = 0
#   isPrime = True

#   while primes[j] * primes[j] <= i:
#     if not i % primes[j]:
#       isPrime = False
#       break
#     j += 1

#   if isPrime:
#     primes.append(i)

# print(primes)


