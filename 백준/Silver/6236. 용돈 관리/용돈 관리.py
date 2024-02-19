input = open(0).readline

day_cnt, take_out_cnt = map(int,input().split())

days = [int(input()) for _ in range(day_cnt)]

start = max(days)
end = 10**9

while start <= end:
    mid = (start + end) // 2
    
    cnt = 0
    left = 0
    
    for i in days:
        if i <= left:
            left -= i
        else:
            cnt += 1
            left = mid - i
    
    if cnt <= take_out_cnt:
        end = mid - 1
    else:
        start = mid + 1
        
print(start)