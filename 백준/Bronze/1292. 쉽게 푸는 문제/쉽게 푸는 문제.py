input = open(0).readline

a = []

for i in range(47):
    a += [i]*i

s, e = map(int, input().split())

print(sum(a[s-1:e]))