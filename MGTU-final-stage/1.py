from math import sqrt

exp = input()
x, y = map(int, input().split())

x_idx = exp.index('x')
A = int(exp[:x_idx])

y_idx = exp.index('y')
B = int(exp[x_idx+1:y_idx])

equal_idx = exp.index('=')
C = int(exp[y_idx+1:equal_idx])

if A == 0 and B == 0 and C != 0: # крайний случай
	print('NO')
	exit()

if A * x + B * y + C == 0:
	print('YES')
else:
	distance = int(abs(A * x + B * y + C) / sqrt(A * A + B * B))

	print('NO', distance)