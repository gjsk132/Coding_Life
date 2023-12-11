import sys
n = int(sys.stdin.readline())
cnt = {}
sm = 0
for i in range(n):
    now = int(sys.stdin.readline())
    sm += now
    if not now in cnt:
        cnt[now] = 1
    else:
        cnt[now] += 1
print(int(round(sm/float(n),0)))

hi = max(cnt.values())
hn = []
cnt = dict(sorted(cnt.items()))
tag = False

for k, v in zip(cnt.keys(), cnt.values()):
    # compute median
    if not tag:
        n -= 2*v
        if n < 0:
            print(k)
            tag = True
    
    # compute mode
    if hi == v:
        hn.append(k)
        
print(hn[0] if len(hn)==1 else sorted(hn)[1])

print(max(cnt.keys())-min(cnt.keys()))