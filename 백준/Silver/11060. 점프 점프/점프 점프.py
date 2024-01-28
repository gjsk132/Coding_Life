n = int(input())
dp = [1001]*n
dp[0] = 0

for point, area in zip(range(n), map(int,input().split())):
    for i in range(point+1, point+area+1):
        if i >= n:
            break
        dp[i] = min(dp[i], dp[point]+1)
        
print(-1 if dp[-1] == 1001 else dp[-1])