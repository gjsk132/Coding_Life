from collections import deque

def solution(bridge_length, weight, truck_weights):
    
    time = 0
    
    waiting = deque(truck_weights)
    
    now_weight = 0
    
    # run : (다리에서 진입한 시간, 무게)
    run = deque([])
    
    while waiting or run:
        
        # 1초 지나서
        time += 1
        
        # 다리에 있는 트럭이 내려갔는지 확인
        if run:
            if run[0][0] == time - bridge_length:
                _, finish_t_w = run.popleft()
                now_weight -= finish_t_w
        
        # 다리에 올라갔는지 확인
        if waiting:
            if weight >= now_weight + waiting[0]:
                t_w = waiting.popleft()
                now_weight += t_w
                run.append((time, t_w))

    return time