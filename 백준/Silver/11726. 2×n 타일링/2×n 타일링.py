input = open(0).readline

n = int(input())

dp = [0 for _ in range(max(n+1,3))]
dp[1] = 1 #세로 1개
dp[2] = 1

for i in range(2, n+1):
    dp[i] += dp[i-2] + dp[i-1]

print(dp[-1]%10007)