n = int(input())


res = []

for i in range(n):
	r, g, b = map(int, input().split())

	arr_bulb = [r, g, b]

	amount_bulb = sum(arr_bulb)
	top_bound = (amount_bulb + 1) // 2

	right_bulb = list(filter(lambda bulb: bulb <= top_bound, arr_bulb))


	verdict = 'Yes' if len(right_bulb) == len(arr_bulb) else 'No'

	res.append(verdict)


print(*res, sep="\n")