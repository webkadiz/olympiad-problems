n = int(input())

n = bin(n)[2:]

ans = []

for char in n:
	char = int(char) ^ 1

	ans.append(str(char))


print( int(''.join(ans), 2) )