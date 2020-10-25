t = int(input())

ans = []
for j in range(t):
        
    n, m = map(int, input().split())

    rows = [list(map(int, input().split())) for i in range(n)]
    cols = [list(map(int, input().split())) for i in range(m)]

    first_col_set = set()
    first_col_list = []
    first_col_sum = 0
    for i in range(n): 
        first_col_list.append(rows[i][0])
        first_col_set.add(rows[i][0])
        first_col_sum += rows[i][0]

    for col in cols:
        if set(col) == first_col_set:
            original_first_col = col
            break
    
    for i, original_el in enumerate(original_first_col):
        idx = first_col_list.index(original_el)
        
        first_col_list[idx], first_col_list[i] = first_col_list[i], first_col_list[idx]
        rows[idx], rows[i] = rows[i], rows[idx]

    ans.append(rows)


for rows in ans:
    [print(*row) for row in rows]
