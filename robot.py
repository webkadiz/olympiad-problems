

def print_coords(dir, intersect = 0):
	global coordX, coordY

	print((coordX, coordY), dir, '+1' if intersect else '')



for i in range(2, 12):

	

	n = k = i

	coordX = 11
	coordY = -11
	for j in range(5):
		for z in range(6): 
			if z == 0:
				coordY += n
				print_coords('up', 1 if coordX % 5 == 0 else 0)
			elif z == 1:
				coordX += n
				print_coords('right', 1 if coordY % 5 == 0 else 0)
			elif z == 2:
				n += k
			elif z == 3:
				coordY -= n
				print_coords('bottom')
			elif z == 4:
				coordX -= n
				print_coords('left', 1 if coordY % 5 == 0 else 0)
			elif z == 5:
				n += k


	print('=============================================================================', i)