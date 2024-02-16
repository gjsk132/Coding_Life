input = open(0).readline

tree_cnt, need_len = map(int,input().split())

trees = list(map(int,input().split()))

start = 1
end = max(trees)

while start <= end:
    cut_len = 0
    
    mid = (start + end) // 2
    
    for i in trees:
        if i <= mid:
            continue
        cut_len += i-mid
    
    if cut_len < need_len:
        end = mid-1
    else:
        start = mid+1
    
print(end)