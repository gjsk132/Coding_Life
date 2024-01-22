input = open(0).readline

num, ad = map(int,input().split())
nlist = [0]+list(map(int,input().split()))

for i in range(num):
    nlist[i+1] += nlist[i]

for i in range(ad):
    s, e = map(int,input().split())
    print(nlist[e]-nlist[s-1])