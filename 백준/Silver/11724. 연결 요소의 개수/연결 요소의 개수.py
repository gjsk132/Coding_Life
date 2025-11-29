from collections import deque

input = open(0).readline

nodes, lines = map(int, input().split())

board = [[] for _ in range(nodes+1)]

check = [False for _ in range(nodes+1)]

for _ in range(lines):
    s, e = map(int, input().split())

    board[s].append(e)
    board[e].append(s)

dq = deque([])

answer = 0

for i in range(1, nodes+1):
    if check[i]:
        continue

    answer += 1

    dq.append(i)
    check[i] = True

    while dq:
        n = dq.popleft()
        for b in board[n]:
            if check[b]:
                continue
            check[b] = True
            dq.append(b)

print(answer)