import re

exp = input()

exp = re.sub('\+', ' + ', exp)
exp = re.sub('\-', ' - ', exp)
exp = re.sub('\*', ' * ', exp)
exp = re.sub('\/', ' / ', exp)


print(exp)