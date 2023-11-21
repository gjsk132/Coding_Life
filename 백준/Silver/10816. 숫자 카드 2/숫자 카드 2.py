input = open(0).readline

n = int(input())
nlist = sorted(map(int, input().split()))

m = int(input())
mlist = list(map(int, input().split()))

check = {}

for i in nlist:
    if i in check:
        check[i] += 1
    
    else: check[i] = 1
    
for i in mlist:
    if not i in check:
        print(0, end=" ")
    else:
        print(check[i], end=" ")