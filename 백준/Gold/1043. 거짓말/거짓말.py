input = open(0).readline
people, party = map(int,input().split())

known = list(map(int,input().split()))
known.pop(0)
known = set(known)

connect = {}
check = set()

for i in range(1,people+1):
    connect[i] = set()

info = []

for i in range(party):
    pty = list(map(int,input().split()))
    info.append(set(pty[1:]))
    for start in pty[1:]:
        for end in pty[1:]:
            if start==end:
                continue
            connect[start].add(end)

while known:
    now = known.pop()
    if not now in check :
        check.add(now)
        known = known.union(connect[now])

result = 0

for i in info:
    if i.difference(check):
        result += 1
        
print(result)