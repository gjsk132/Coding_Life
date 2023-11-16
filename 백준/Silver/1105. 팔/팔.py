input = open(0).readline
l,r = input().split()

result = 0

if len(l)==len(r):
    for i in range(len(l)):
        if l[i]==r[i]:
            if l[i]=='8':
                result += 1
        else:
            break;

print(result)