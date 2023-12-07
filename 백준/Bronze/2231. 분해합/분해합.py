import sys
t = int(sys.stdin.readline())
for i in range(max(1,t-(t//10+1)*9), t+2):
    if t == i + sum(map(int,str(i))):
        break
print(0 if i==t+1 else i)