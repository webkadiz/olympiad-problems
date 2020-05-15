N, M = map(int, input().split())
m = list(map(int, input().split()))

max_el = 0
comb = set()

for el_m in m:
	
	new_comb = set()
	for el_comb in comb:
		new_comb.add(el_m + el_comb)

	comb = comb | new_comb
	comb = comb | {el_m}


for el_comb in comb:
	if el_comb > max_el and el_comb <= M:
		max_el = el_comb



print(max_el)


