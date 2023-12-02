input = open(0).readline
node = int(input())
link = int(input())

move = [[] for _ in range(node+1)]

for i in range(link):
    n1, n2 = map(int, input().split())
    move[n1].append(n2)
    move[n2].append(n1)

visited = [0]*(node+1)

def dfs(pre):
    visited[pre] = 1
    cnt = 0
    for i in move[pre]:
       if visited[i] == 0:
           visited[i] = 1
           cnt += dfs(i) + 1
    
    return cnt

print(dfs(1))