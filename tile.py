m = int(input())
x = int(input())
y = int(input())
w = int(input())
h = int(input())

ky = 1
kx = 1

h -= 10 - y % 10
w -= 10 - x % 10

ky += (h + 9) // 10	if h > 0 else 0
kx += (w + 9) // 10 if w > 0 else 0

print(ky * kx)