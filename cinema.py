import math

k = int(input())
left = right = top = bottom = None


sqrt_c = math.ceil(math.sqrt(k))

bound_l = ((sqrt_c - 1) ** 2) + 1
bound_r = sqrt_c ** 2
bound_r_below = (sqrt_c + 1) ** 2
bound_r_above = bound_l - 1




# compute right
if k < bound_r: right = k + 1

# compute left
if k > bound_l: left = k - 1


# compute top
if k != bound_r and k != bound_l:
	shift = bound_r - k
	top = bound_r_above - (shift - 1)

# compute bottom
shift = bound_r - k
bottom = bound_r_below - (shift + 1)


print(left, right, top, bottom)