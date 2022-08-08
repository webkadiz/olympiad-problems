import sys
import re

vars_ = {}

try:
    for line in sys.stdin:
        line = line.strip()
        equalIdx = line.find('=')

        if ~equalIdx:
            var1 = line[:equalIdx]
            var2 = line[equalIdx+1:]

            if bool(re.search('\d', var2)):
                var2 = int(var2)

            vars_.setdefault(var1, [0])

            if type(var2) != int:
                vars_.setdefault(var2, [0])
                # print(vars_)
                var2Value = vars_[var2][-1]
                vars_[var1][-1] = var2Value
                print(var2Value)
            else:
                vars_[var1][-1] = var2

            # print(line)
        elif line == '{':
            for key in vars_:
                cur = vars_[key][-1]
                vars_[key].append(cur)
        elif line == '}':
            varsForDelete = []
            for key in vars_:
                vars_[key].pop()

                if len(vars_[key]) == 0:
                    varsForDelete.append(key)

            for key in varsForDelete:
                del vars_[key]
except StopIteration:
    pass
