def solution(s):
    
    s_split = s.split()
    
    up = int(s_split[0])
    down = int(s_split[0])
    
    for i in range(1,len(s_split)):
        if (int(s_split[i])>up):
            up = int(s_split[i])
        elif (int(s_split[i])<down):
            down = int(s_split[i])
    
    answer = str(down)+' '+str(up)
    
    return answer