input = open(0).readline

gap = int(input())
max_weight = (gap)//2 + 1

def binary_search(start, end, num):
        
    if start > end:
        return 0
    
    mid = (start + end) // 2

    tmp = num**2 - mid**2

    if tmp == gap:
        return num
    elif tmp < gap:
        end = mid - 1
    else:
        start = mid + 1

    return binary_search(start, end, num)
    
ans = []

for weight in range(1, max_weight+1):
    if (result := binary_search(1, weight, weight)):
        ans.append(result)

if ans:
    print(*ans)
else:
    print(-1)