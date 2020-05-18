from math import inf
nums = list(map(int, input().split()))

signs = { '+': 1, '-': 2, '*': 3, '/': 4, '%': 5, '=': 0 }

anss = []


def comb(nums, exp, wasEq):

	if not nums:
		try:
			res = eval(exp)
		except:
			res = 0
		if type(res) == bool and eval(exp):
			anss.append(exp)
			return
		return

	cur, nrest = str(nums[0]), nums[1:]

	if wasEq:
		comb(nrest, exp + '+' + cur, True)
		comb(nrest, exp + '-' + cur, True)
		comb(nrest, exp + '*' + cur, True)
		comb(nrest, exp + '/' + cur, True)
		comb(nrest, exp + '%' + cur, True)
	else:
		
		comb(nrest, exp + '+' + cur, False)
		comb(nrest, exp + '-' + cur, False)
		comb(nrest, exp + '*' + cur, False)
		comb(nrest, exp + '/' + cur, False)
		comb(nrest, exp + '%' + cur, False)
		comb(nrest, exp + '==' + cur, True)
		

comb(nums[1:], str(nums[0]), False)

print(anss)

min_v = inf

for ans in anss:
	ves = 0
	for char in ans:
		ves += signs.get(char, 0)


	if ves < min_v:
		min_v = ves
		real_ans = ans

real_ans = real_ans.replace('==', '=')
print(real_ans)

for char in real_ans:

	if 48 <= ord(char) <= 57:
		continue

	print(char, end='')
print()
