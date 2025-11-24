input = open(0).readline

cases = int(input())

cases_list = [int(input()) for _ in range(cases)]

limit = max(cases_list)+1

dp = [1 for _ in range(limit)]

for i in range(4, limit):
    dp[i] = dp[i-3]+dp[i-2]

for c in cases_list:
    print(dp[c])