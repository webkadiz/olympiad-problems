

def binpow(num, pow):

	if not pow:
		return 1

	if pow % 2 == 1:
		return binpow(num, pow - 1) * num
	else:
		x = binpow(num, pow / 2)

		return x * x



print(binpow(4, 2))