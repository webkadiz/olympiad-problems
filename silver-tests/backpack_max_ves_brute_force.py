N, M = map(int, input().split())
m = list(map(int, input().split()))
cnt_slice = len(m)

max_ves_value = 0


def max_ves(s = 0, n = 0, max_n = cnt_slice):
	global max_ves_value

	if n == max_n:
		if s <= M and s > max_ves_value:
			max_ves_value = s
		return

	if s <= M:
		max_ves(s + m[n], n + 1)
		max_ves(s + 0, n + 1)
	
max_ves()

print(max_ves_value)