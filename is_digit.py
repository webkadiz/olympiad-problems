import re

char = input()


print(bool(re.search('[0-9]', char)))