import sys
t = int(sys.stdin.readline())
for i in range(1, t+2):
    if t == i + sum(map(int,str(i))):
        break
print(0 if i==t+1 else i)