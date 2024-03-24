input = open(0).readline

num_cnt = int(input())

nlist = list(map(int,input().split()))

memo = [0 for _ in range(num_cnt)]

for i, x in enumerate(nlist):
    high = 1
    for j, y in enumerate(nlist[:i]):
        if x > y:
            high = max(memo[j]+1, high)
    memo[i] = high

print(memo[memo.index(max(memo))])