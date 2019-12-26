k, n, m = map(int, input().split(' '))
arr_s = map(int, input().split(' '))
arr_s = list(arr_s)
s1 = arr_s[0]

close_k = 0
sum_s = sum(arr_s)



while s1 * n / sum_s < m:
	

	mx = max(arr_s[1:])
	arr_s.remove(mx)

	close_k += 1
	sum_s = sum(arr_s)



print(close_k)