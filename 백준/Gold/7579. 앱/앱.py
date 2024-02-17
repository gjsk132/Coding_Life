input = open(0).readline

sample, max_memory = map(int,input().split())

limit = 10**4

sum_cost = [0 for _ in range(limit+1)]

for use_m, use_c in zip([m for m in map(int,input().split())],[c for c in map(int,input().split())]):
    for now_c in reversed(range(use_c, limit+1)):
        sum_cost[now_c] = max(sum_cost[now_c], sum_cost[now_c-use_c]+use_m)

for i in range(limit+1):
    if sum_cost[i] >= max_memory:
        print(i)
        break