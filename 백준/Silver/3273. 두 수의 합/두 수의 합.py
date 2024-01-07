input = open(0).readline
size = int(input())
num = sorted(list(map(int,input().split())))
target = int(input())

start, end, result = 0, size-1, 0

while start < end:
     
    add = num[start] + num[end]  
    
    if add > target:
        end -= 1
        
    elif add < target:
        start += 1
        
    else:
        start += 1
        end -= 1
        result += 1
    
print(result)