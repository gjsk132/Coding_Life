from collections import deque

def solution(priorities, location):
    dq = deque(priorities)
    
    next_run = max(dq)
    
    run_cnt = 0
    
    while True:
        now_p = dq.popleft()
        location -= 1
        
        if next_run == now_p:
            run_cnt += 1
            next_run = max(dq) if dq else 0
    
            if location == -1:
                return run_cnt
            
            continue
            
        dq.append(now_p)
        
        if location == -1:
            location = len(dq) - 1
    