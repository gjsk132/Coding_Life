dp = [10001 for _ in range(5001)]
dp[3], dp[5] = 1, 1

N = int(input())
cnt = 6
while cnt <= N:
    dp[cnt] = min(dp[cnt-3], dp[cnt-5]) + 1
    cnt += 1

print(-1 if dp[N]>10000 else dp[N])