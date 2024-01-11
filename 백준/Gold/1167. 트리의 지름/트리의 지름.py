from collections import defaultdict, deque

input = open(0).readline

node = int(input())

tree = [{} for _ in range(node+1)]
tree_re = [{} for _ in range(node+1)]

for i in range(node):
    cost_info = list(map(int,input().split()))
    start = cost_info.pop(0)
    
    while True:
        end = cost_info.pop(0)
        if end == -1:
            break
        cost = cost_info.pop(0)
        tree[start][end] = cost
        tree_re[start][cost] = end

def bfs(v=1):
    check = [False for i in range(node+1)]

    dq = deque([(v,0)])
    start = v
    high = 0

    while dq:
        p, c = dq.popleft()
        if check[p]:
            continue
    
        if c > high:
            start = p
            high = c
        
        check[p] = True
        
        for k, v in zip(tree[p].keys(), tree[p].values()):
            dq.append([k, v+c])
    
    return [start, high]

print(bfs(bfs()[0])[1])