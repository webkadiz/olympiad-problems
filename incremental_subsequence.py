from math import inf

n = int(input())
seq = list(map(int, input().split()))

k = [0] * n



for i in range(n):
	k[i] = 0
	mem = inf
	
	for j in range(i, -1, -1):
		if seq[j] < mem:
			k[i] += 1
			mem = seq[j]

mk = 0
mk_idx = -1

for i in range(n):
	if k[i] > mk:
		mk = k[i]
		mk_idx = i

ans_seq = [0] * mk
mem = inf
j = mk-1
for i in range(mk_idx, -1, -1):
		if seq[i] < mem:
			mem = seq[i]
			ans_seq[j] = mem
			j -= 1

print(mk)
print(*ans_seq)