n, s, m = map(int,input().split())
volume = list(map(int,input().split()))
dp = [set([s])] + [set() for _ in range(n)]

for k, v in enumerate(volume):
    for j in dp[k]:
        if j == -1:
            continue
        dp[k+1].add(j+v if j+v <= m else -1)
        dp[k+1].add(j-v if j-v >= 0 else -1)

print(max(dp[-1]) if dp[-1] else -1)