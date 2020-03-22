from time import time

m, n = map(int, input().split())

start = time()

n += 1
primes = [True] * n
primes[0] = primes[1] = False

sqrtN = int(n ** 0.5) + 1

for i in range(2, sqrtN):
    if primes[i]:
        primes[i] = True

        for j in range(i*i, n, i):
            primes[j] = False

wasSimple = False



#for i in range(m, n):

#    if primes[i]:
#        wasSimple = True
#        print(i)

#if not wasSimple:
#    print("Absent")


end = time()


print(end - start)



