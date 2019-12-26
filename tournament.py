n = int(input())

teams = list(range(1, n + 1))

losers = []

for i in range(2, n + 1, 2):

	print(teams)

	for j in range(n//i):
		winner = int(input())

		first = teams[j * 2]
		second = teams[j * 2 + 1]

		losers.append(first if winner == 2 else second)

	for loser in losers:
		teams.remove(loser)

	losers = []
	
print(teams[0])