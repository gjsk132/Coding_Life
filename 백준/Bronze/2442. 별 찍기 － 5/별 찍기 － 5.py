input = open(0).readline

cnt = int(input())

tmp = [2*i+1 for i in range(cnt)]

for i in range(cnt):
    print(" "*(cnt-i-1)+"*"*tmp[i])