input = open(0).readline

N = int(input())
members = [input().split() for i in range(N)]
members.sort(key = lambda x: int(x[0]))

for m in members:
    print(" ".join(m))