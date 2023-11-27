input = open(0).readline
num, target = map(int,input().split())
cnt = 0
while target > num:
    if (target%2==0):
        target //= 2
        cnt+=1
        continue
    elif (target%10==1):
        target //= 10
        cnt+=1
    else:
        break

print(cnt+1 if target==num else -1)