n, s = map(int, input().split())
numbers = list(map(int, input().split()))

ans = ''

l_numbers = len(numbers)

def exp(k, sum, res):

  if k == l_numbers:
    if sum == s:
      print(res + '=' + str(s))
      exit()
    return

  exp(k + 1, sum + numbers[k], res + '+' + str(numbers[k]))    
  exp(k + 1, sum - numbers[k], res + '-' + str(numbers[k]))


exp(1, numbers[0], str(numbers[0]))


print('No solution')

