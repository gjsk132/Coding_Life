input = open(0).readline

total = int(input())
cnt = int(input())

tmp = [i+1 for i in range(cnt)]

tmp[-1] += total - sum(tmp)

for t in tmp:
    print(t)