n,m = map(int,input().split())

dp =[list(map(int,input().split())) for _ in range(n)]

for x in range(n):
    for y in range(m):
        dp[x][y] += max(0 if y == 0 else dp[x][y-1], 0 if x == 0 else dp[x-1][y])

print(dp[-1][-1])