input = open(0).readline

stairs = int(input())

stairs_value = [0] + [int(input()) for _ in range(stairs)]

if stairs == 1:
    print(stairs_value[1])
else:
    dp = [0 for i in range(stairs+1)]
    dp[1] = stairs_value[1]
    dp[2] = sum(stairs_value[1:3])

    for n in range(3, stairs+1):
        dp[n] = max(dp[n-2], dp[n-3]+stairs_value[n-1])+stairs_value[n]

    print(dp[-1])