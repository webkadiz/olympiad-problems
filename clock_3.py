a = float(input())

hours = a // 30

a = a - int(a // 30) * 30
minutes = int(a) * 2

a = a - int(a)
seconds = a * 120

print(int(hours), int(minutes), int(seconds))