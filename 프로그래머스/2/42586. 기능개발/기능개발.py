def solution(progresses, speeds):
    answer = []
    
    finished = []
    
    for p, s in zip(progresses, speeds):
        left = 100 - p
        
        finished.append(left//s + (1 if left%s else 0))
    
    day = finished[0]
    cnt = 0
    
    for f in finished:
        if f > day:
            answer.append(cnt)
            cnt = 1
            day = f
        else:
            cnt += 1
    
    answer.append(cnt)
    
    return answer