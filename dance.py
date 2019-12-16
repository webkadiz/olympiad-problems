n = int(input())
number = int(input())
k = int(input())

k = k % n

if number % 2:
  endmpos = (number + k) % n + 1
else:
  endmpos = (number - k) % n + 1


endrpos = (endmpos + 1) % n + 1
endlpos = (endmpos + n - 1) % n + 1

if number % 2:
  lnum = (endlpos + n - k - 1) % n
  rnum = (endrpos + n - k - 1) % n


print(lnum, rnum)