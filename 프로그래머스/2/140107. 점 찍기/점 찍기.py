import math

def solution(k, d):
    
    answer = 0
    
    for i in range(0, d+1, k):
        length = int(math.sqrt(pow(d, 2)-pow(i, 2)))
        answer += (length//k) + 1
    
    return answer