import queue

n = int(input())

graph = [list(map(int, input().split())) for i in range(n)]

start, end = map(int, input().split())
start -= 1
end -= 1
q = queue.Queue()

q.put(start)
used = [0] * n
d = [0] * n
p = [0] * n

used[start] = 1
d[start] = 1
p[start] = -1
while not q.empty():
    cur = q.get()
    
    for i in range(n):
        if graph[cur][i]:
            if not used[i]:
                used[i] = 1
                d[i] = d[cur] + 1
                p[i] = cur
                q.put(i)
                

if not d[end]:
    print(-1)
else:
    path = []
    to = end
    i = 0
    while p[to] != -1:
        path.append(to + 1)
        to = p[to]
        i += 1
    path.append(to + 1)
    print(i)
    print(*path[::-1])
    

