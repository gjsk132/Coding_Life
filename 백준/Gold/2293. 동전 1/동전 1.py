input = open(0).readline

cnt, target = map(int,input().split())

coins = [int(input()) for _ in range(cnt)]

dp = [0]*(target+1)

for c, m in ((coin, money) for coin in coins for money in range(1,target+1)):
    dp[m] += 1 if c==m else dp[m-c] if m > c else 0
    
print(dp[-1])