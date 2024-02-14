n, k = map(int,input().split())

k = min(n-k, k)

tmp1 = 1
tmp2 = 1

while k:
    tmp1*= n
    tmp2*= k
    
    n -= 1
    k -= 1

print(tmp1//tmp2)