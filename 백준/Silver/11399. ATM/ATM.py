n = input()
nlist = reversed(sorted(list(map(int,input().split()))))
total = 0

for k, v in enumerate(nlist):
    total += v*(k+1)

print(total)