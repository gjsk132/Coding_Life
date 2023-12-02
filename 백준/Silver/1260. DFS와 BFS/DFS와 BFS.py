from collections import deque
input = open(0).readline
node, link, s_node = map(int, input().split())

move = [[] for _ in range(node+1)]

for info in range(link):
    n1, n2 = map(int, input().split())
    move[n1].append(n2)
    move[n2].append(n1)

for k, v in enumerate(move):
    move[k] = sorted(v)

visited = [0]*(node+1)
visited[s_node] = 1

def dfs(pre):
    print(pre, end=" ")
    for i in move[pre]:
        if visited[i] == 0:
            visited[i] = 1
            dfs(i)

dfs(s_node)

print()

visited = [0]*(node+1)

visited[s_node] = 1
deq = deque([s_node])

while len(deq)!=0:
    now = deq.popleft()
    print(now, end =" ")
    
    for i in move[now]:
        if visited[i] == 0:
            visited[i] = 1
            deq.append(i)