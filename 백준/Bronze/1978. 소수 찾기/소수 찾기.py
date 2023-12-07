import sys
n = sys.stdin.readline()
cnt = 0
for i in map(int, sys.stdin.readline().split()):
    if i <= 1:
        continue
    prime = True
    j = 2
    while j**2 <= i:
        if i%j == 0:
            prime = False
            break
        j+=1
    if prime:
        cnt+=1
print(cnt)