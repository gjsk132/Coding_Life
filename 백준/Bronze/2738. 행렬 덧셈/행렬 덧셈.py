input = open(0).readline

n, m = map(int, input().split())

table = [[0]*m for _ in range(n)]

for i in range(n):
    for k, v in enumerate(list(map(int, input().split()))):
        table[i][k] += v

for i in range(n):
    for k, v in enumerate(list(map(int, input().split()))):
        table[i][k] += v

for _ in table:
    print(" ".join(map(str, _)))