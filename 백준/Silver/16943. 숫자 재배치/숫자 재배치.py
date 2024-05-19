from collections import defaultdict

input = open(0).readline

given_num, limit = map(int,input().split())
num_cnt = defaultdict(int)
num_len = 0

for num in str(given_num):
    num_cnt[num] += 1
    num_len += 1

num_kinds = sorted(num_cnt.keys(), reverse=True)
num_combs = []

def backtracking():
    if len(num_combs) == num_len:
        return int("".join(map(str, num_combs)))
    
    for n in num_kinds:
        if num_cnt[n] == 0:
            continue
        num_combs.append(n)
        num_cnt[n] -= 1
        result = backtracking()
        if result and result < limit:
            return result
        num_combs.pop()
        num_cnt[n] += 1

answer = backtracking()
print(-1 if len(str(answer)) != num_len else answer)