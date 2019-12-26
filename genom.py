sa = input()
sb = input()
k = 0

for i in range(len(sa) - 1):
	pair = sa[i:i+2]

	if ~sb.find(pair):
		k += 1

print(k)