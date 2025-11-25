input = open(0).readline

target = int(input())

limit = float("inf")

dp = [limit for _ in range(target+1)]

dp[0] = 0
dp[1] = 1

for i in range(2, target+1):
    for n in range(1,224):
        if i < n*n:
            break
        dp[i] = min(dp[i], dp[i-n*n]+1)

print(dp[-1])