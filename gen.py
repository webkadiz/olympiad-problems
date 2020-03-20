import random

sign = ['N', 'W', 'E', 'S', '.']
op = open('test', 'w')

n = 5000
op.write(str(n) + '\n')

for i in range(n):
    rand = random.randint(1, 10 ** 3)    
    op.write(str(rand))
    op.write(' ')

op.close()
