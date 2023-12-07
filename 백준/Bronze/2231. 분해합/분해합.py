import sys
t = int(sys.stdin.readline())
for i in range(1, t+2):
    if i==t+1:
        break
    n = i + sum(map(int,str(i)))
    if n == t:
        break
print(0 if i==t+1 else i)