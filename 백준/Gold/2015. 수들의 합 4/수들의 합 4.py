from collections import defaultdict

input = open(0).readline

n, target = map(int,input().split())

before = 0
prefix_sum = [(before:= before + i) for i in list(map(int,input().split()))]

cnt = defaultdict(int)

ans = prefix_sum.count(target)

for ps in prefix_sum:
    ans += cnt[ps-target]
    cnt[ps] += 1
    
print(ans)