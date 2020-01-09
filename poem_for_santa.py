t = int(input())

ans = []


for i in range(t):
	n, s = map(int, input().split())
	parts = list(map(int, input().split()))

	p_sum = 0

	last_idx = -1

	for i, part in enumerate(parts):

		p_sum += part

		if p_sum > s:
			last_idx = i - 1
			break

	else:
		ans.append(0)
		continue


	if not ~last_idx:
		ans.append(1)
		continue

	amount_to_pos = {last_idx + 1: last_idx + 1}

	for j in range(last_idx, -1, -1):

		cur_idx = j
		top_sum = parts[j]
		cur_sum = 0

		while cur_idx + 1 < len(parts) and cur_sum + parts[cur_idx + 1] <= top_sum:
			cur_idx += 1
			cur_sum += parts[cur_idx]



		amount_parts = j + cur_idx - j
 
		amount_to_pos[amount_parts] = j + 1


	if int(max(amount_to_pos.keys())) == last_idx + 1:
		res = 0 

	else: 
		res = amount_to_pos[max(amount_to_pos.keys())]

	ans.append(res)





print(*ans, sep="\n")