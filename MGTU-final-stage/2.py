exp = input()

exp_for_eval_template = exp.replace('=', '==')

ans = []

for a in range(2):
	for b in range(2):
		for c in range(2):
			exp_for_eval = exp_for_eval_template

			exp_for_eval = exp_for_eval.replace('a', str(a))
			exp_for_eval = exp_for_eval.replace('b', str(b))
			exp_for_eval = exp_for_eval.replace('c', str(c))

			res = int(eval(exp_for_eval))
			ans.append(res)

print(*ans, sep='')