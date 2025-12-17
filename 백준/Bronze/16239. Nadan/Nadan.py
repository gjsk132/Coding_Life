input = open(0).readline

total = int(input())
cnt = int(input())

tmp = [i+1 for i in range(cnt)]

now = sum(tmp)

while now < total:
    for i in range(cnt):
        if not i == cnt-1 and tmp[i+1] == tmp[i] + 1:
            continue
        else:
            tmp[i] += 1
            break
    now += 1

for t in tmp:
    print(t)