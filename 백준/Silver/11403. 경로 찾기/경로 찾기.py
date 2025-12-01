from collections import deque

input = open(0).readline

size = int(input())

lines = [[] for _ in range(size)]

for s in range(size):
    for e, flag in enumerate(list(map(int, input().split()))):
        if flag:
            lines[s].append(e)
        
def check_approach(start_node):
    check = [0 for _ in range(size)]

    dq = deque([start_node])
    
    while dq:
        now_node = dq.popleft()

        for next_node in lines[now_node]:
            if check[next_node]:
                continue
            check[next_node] = 1
            dq.append(next_node)

    return " ".join(map(str, check))

for i in range(size):
    print(check_approach(i))