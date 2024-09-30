from collections import defaultdict

input = open(0).readline

listen, watch = map(int,input().split())

answer = []

cnt = defaultdict(int)

for i in range(listen+watch):
    cnt[input().rstrip()] += 1

for k, v in cnt.items():
    if v == 2:
        answer.append(k)

print(len(answer))
for a in sorted(answer):
    print(a)