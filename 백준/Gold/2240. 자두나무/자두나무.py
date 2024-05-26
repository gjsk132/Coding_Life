input = open(0).readline

time, can_change = map(int,input().split())

dp = [[0]*(can_change+1) for _ in range(time)]

for t in range(time):
    for set in range(int(input())-1, can_change+1, 2):
        dp[t][set] += 1

for t in range(1, time):
    for idx in range(min(t, can_change)+1):
        if idx == 0:
           dp[t][idx] += dp[t-1][idx]
           continue

        dp[t][idx] += max(dp[t-1][idx-1], dp[t-1][idx])

print(max(dp[-1]))