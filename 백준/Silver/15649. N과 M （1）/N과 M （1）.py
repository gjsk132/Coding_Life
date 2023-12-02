n, m = map(int, input().split())    

mark = []

def back(cnt):
    if cnt == 0:
        print(*mark)
        return
    
    for i in range(1, n+1):
        if not i in mark:
            mark.append(i)
            back(cnt-1)
            mark.pop()
            
back(m)