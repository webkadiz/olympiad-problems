x = int(input())

y = 16

a = x
b = y

while x != y:  
  if x > y:
    x = x - y
  else:
    y = y -x

z = a * b / y
print(z)