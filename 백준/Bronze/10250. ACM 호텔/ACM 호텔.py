import sys
for i in range(int(sys.stdin.readline())):
    h,w,n = map(int, sys.stdin.readline().split())
    if (n%h == 0):
        print(h*100+n//h)
    else:
        print(n%h*100+n//h+1)