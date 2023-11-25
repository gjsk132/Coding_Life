input = open(0).readline
colors = int(input())

clist = [0]*colors

memo =[ [0 for i in range(100)] for j in range(100)]

for i in range(colors):
    x, y = map(int, input().split())
    for nx in range(x, x+10):
        for ny in range(y, y+10):
            memo[nx][ny] = 1
        
        
result = 0

for i in memo:
    result += sum(i)

print(result)