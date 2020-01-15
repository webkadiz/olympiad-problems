import random

sign = ['N', 'W', 'E', 'S', '.']
op = open('test', 'w')

op.write('30 30\n')

for i in range(30):
    for j in range(30):
        rand = random.randrange(5)

        op.write(sign[rand])
    op.write('\n')

op.close()
