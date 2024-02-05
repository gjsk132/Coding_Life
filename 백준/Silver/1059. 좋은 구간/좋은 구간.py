size = int(input())
num = sorted(list(map(int,input().split())))
target = int(input())

s, e = 0, 0
flag = False

for e in num:
    if e > target:
        flag = True
        break
    else:
        s = e
        
print(0 if target==s or target == e else (target-s)*(e-target)-1)