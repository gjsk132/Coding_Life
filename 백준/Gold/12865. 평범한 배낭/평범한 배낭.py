input = open(0).readline

loads, bag = map(int,input().split())

dp = [[0 for i in range(bag+1)] for _ in range(loads+1)]

for step in range(loads):
    kg, value = map(int,input().split())
    
    for p in range(bag+1):
        dp[step+1][p] = max(dp[step][p], dp[step][p-kg]+value if p >=kg else 0)
    
print(dp[-1][-1])