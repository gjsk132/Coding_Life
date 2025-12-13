from collections import deque

input = open(0).readline

node_cnt = int(input())

parent = [-1]*(node_cnt+1)

lines = [[] for _ in range(node_cnt+1)]

for _ in range(node_cnt-1):
    a, b = map(int, input().split())
    lines[a].append(b)
    lines[b].append(a)

dq = deque([(0, 1)])

while dq:
    pre_n, now_n = dq.popleft()

    for next_n in lines[now_n]:
        if not parent[next_n] == -1:
            continue
        parent[next_n] = now_n
        dq.append((now_n, next_n))

for ans in parent[2:]:
    print(ans)