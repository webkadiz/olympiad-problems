import re

s = input()


print(len(re.findall('[;:]-*[\[\]()]+?', s)))