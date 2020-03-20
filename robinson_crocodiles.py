import sys

n, m = map(int, input().split())

island = [list(input()) for i in range(n)]
k = 0


def cross(i, j):
	global island
	island[i][j] = 'X'


def find_path(i, j, direct):
	global island, k

	# print(i, j, direct)

	if direct == 'OK' or direct == '.':
		return True
	elif direct == 'X':
		return False
	elif direct == 'N':
		for t in range(i - 1, -1, -1):
			if island[t][j] == 'S' or not find_path(t, j, island[t][j]):
				cross(i, j)
				return False
		
		island[i][j] = 'OK'
		k += 1
		return True

	elif direct == 'S':
		for t in range(i + 1, n):
			if island[t][j] == 'N' or not find_path(t, j, island[t][j]):
				cross(i, j)
				return False

		island[i][j] = 'OK'
		k += 1
		return True

	elif direct == 'W':
		for t in range(j - 1, -1, -1):
			if island[i][t] == 'E' or not find_path(i, t, island[i][t]):
				cross(i, j)
				return False

		island[i][j] = 'OK'
		k += 1
		return True

	elif direct == 'E':
		for t in range(j + 1, m):
			if island[i][t] == 'W' or not find_path(i, t, island[i][t]):
				cross(i, j)
				return False

		island[i][j] = 'OK'
		k += 1
		return True


for i in range(n):
	for z in range(m):
		find_path(i, z, island[i][z])

[print(*row, sep="") for row in island]

print(k)
