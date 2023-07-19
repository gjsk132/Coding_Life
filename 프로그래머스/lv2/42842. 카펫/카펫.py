def solution(brown, yellow):
    
    answer = []
    
    for i in range(1, yellow+1):
        if (brown//2 == (i+1)+((yellow/i+1))):
            answer = [int((yellow/i+1)+1), i+2]
            break
    
    return answer