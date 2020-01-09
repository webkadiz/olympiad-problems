import timeit


res = timeit.repeat(
'''
import math

m, n = 1, 10 ** 7

sqrtN = int(math.sqrt(n))

primes = [True] * (n + 1)
primes[0] = primes[1] = False

for i in range(3, sqrtN + 1, 2):
  if primes[i]:
    for j in range(i*i, n + 1, i):
      primes[j] = False

'''
, number=1, repeat=3)


print(res)