

stack = []
real_exit = exit

ans = []

def push(n):
	stack.append(n)
	ans.append('ok')

def pop(n):
	ans.append(stack.pop())

def size(n):
	ans.append(len(stack))

def back(n):
	ans.append(stack[-1])

def clear(n):
	stack.clear()
	ans.append('ok')

def exit(n):
	ans.append('bye')
	print(*ans, sep="\n")
	real_exit()

d = {
	'push': push,
	'pop': pop,
	'size': size,
	'back': back,
	'clear': clear,
	'exit': exit
}

while True:
	command, *value = input().split()
	value = int(value[0]) if value else -1

	d[command](value)

