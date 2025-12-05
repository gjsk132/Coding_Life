from collections import deque

input = open(0).readline

cases = int(input())

for _ in range(cases):
    base, target = map(int, input().split())

    visited = [False] * 10000
    visited[base] = True

    parent = [-1] * 10000
    how = [""] * 10000
    
    dq = deque([base])
    
    while dq:
        now = dq.popleft()

        if now == target:
            break

        # D
        nxt = (now * 2) % 10000
        if not visited[nxt]:
            visited[nxt] = True
            parent[nxt] = now
            how[nxt] = "D"
            dq.append(nxt)

        # S
        nxt = now - 1 if now > 0 else 9999
        if not visited[nxt]:
            visited[nxt] = True
            parent[nxt] = now
            how[nxt] = "S"
            dq.append(nxt)

        # L
        nxt = (now % 1000) * 10 + (now // 1000)
        if not visited[nxt]:
            visited[nxt] = True
            parent[nxt] = now
            how[nxt] = "L"
            dq.append(nxt)

        # R
        nxt = (now // 10) + (now % 10) * 1000
        if not visited[nxt]:
            visited[nxt] = True
            parent[nxt] = now
            how[nxt] = "R"
            dq.append(nxt)
        
    path = []
    cur = target
    while cur != base:
        path.append(how[cur])
        cur = parent[cur]

    print("".join(path[::-1]))