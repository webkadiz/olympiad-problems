def to_dec_num(hex_str):
	return int(hex_str, 16)

def to_hex_str(dec_num):
	return hex(dec_num).upper()[2:]

def diff_mul(mul1, mul2):
	# Возвращает индекс ошибки записи в произведении, если такая ошибка одна, иначе -1
	len_mul1 = len(mul1)
	len_mul2 = len(mul2)
	cnt_wrongs = 0
	idx_wrong = -1

	if len_mul1 != len_mul2:
		return -1

	for i in range(len_mul1):
		if mul1[i] != mul2[i]:
			cnt_wrongs += 1
			idx_wrong = i

		if cnt_wrongs >= 2: return -1
	
	return idx_wrong


def define_rights_numbers(dec_num1, dec_num2, dec_mul):
	div1 = dec_mul / dec_num2 # потенциально правильное число под номером 1
	div2 = dec_mul / dec_num1 # потенциально правильное число под номером 2
	
	if int(div1) == div1:
		return to_hex_str(int(div1)), num2
	elif int(div2) == div2:
		return num1, to_hex_str(int(div2))
	else:
		assert 0



num1 = input()
num2 = input()
mul = input()

dec_num1 = to_dec_num(num1)
dec_num2 = to_dec_num(num2)
dec_mul = to_dec_num(mul)

if dec_mul == 0 and dec_num1 * dec_num2 != 0: # крайний случай
	if len(num1) != 1:
		num1 = 0
	else:
		num2 = 0
	
	print(num1)
	print(num2)
	print(mul)
	exit()
 

hex_mul_right = to_hex_str(dec_num1 * dec_num2) # правильное произведение

idx_wrong = diff_mul(mul, hex_mul_right)

if ~idx_wrong:
	print(num1)
	print(num2)
	print(hex_mul_right)
else: # mul и dec_mul правильные произведения

	# только одно число изменится
	new_num1, new_num2 = define_rights_numbers(dec_num1, dec_num2, dec_mul)
	
	print(new_num1)
	print(new_num2)
	print(mul)
