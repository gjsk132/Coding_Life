def solution(array, commands):
    answer = []
    
    for s, e, idx in commands:
        answer.append(sorted(array[s-1:e])[idx-1])
    
    return answer