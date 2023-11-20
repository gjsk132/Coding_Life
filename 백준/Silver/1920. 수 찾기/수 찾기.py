input = open(0).readline

n = int(input())
nlist = set(map(int,input().split()))

cnt = int(input())
targets = list(map(int,input().split()))

for target in targets:
    print(1) if target in nlist else print(0)