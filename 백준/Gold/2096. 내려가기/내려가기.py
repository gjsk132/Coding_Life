input = open(0).readline
layer = int(input())

low = [[0,0,0], [0,0,0]]
high = [i[:] for i in low]

for i in range(layer):
    p = i%2
    low[p] = list(map(int,input().split()))
    high[p] = [_ for _ in low[p]]
    
    for j in range(3):
        low[p][j] += min(1e9 if j==0 else low[p-1][j-1], low[p-1][j],1e9 if j==2 else low[p-1][j+1])
        high[p][j] += max(0 if j==0 else high[p-1][j-1], high[p-1][j],0 if j==2 else high[p-1][j+1])

print(max(high[layer%2-1]), min(low[layer%2-1]))