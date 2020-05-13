E, F = map(int, input().split())
N = int(input())

max_w = F-E+1
count_ves_max = [0] * (max_w)
count_ves_min = [50001] * (max_w)

def count(count_ves, cond):
    
    for w in range(max_w):

        m = w // 2

        for i in range(1, m+1):
            el = count_ves[i]
            pair_el = count_ves[w-i]

            if cond == 'max':
                if el*pair_el > 0 and el + pair_el > count_ves[w]:
                    count_ves[w] = el + pair_el
            elif cond == 'min':
                if el*pair_el > 0 and el + pair_el < count_ves[w]:
                    count_ves[w] = el + pair_el
        
    return count_ves[max_w-1]

for i in range(N):
    
    p, w = map(int, input().split())
    
    if w > max_w: continue
    
    count_ves_max[w] = p
    count_ves_min[w] = p


res_max = count(count_ves_max, 'max')
res_min = count(count_ves_min, 'min')

if res_max == 0:
    print('This is impossible.')
else:
    print(res_min)
    print(res_max)
