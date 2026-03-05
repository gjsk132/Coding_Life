from heapq import *

def solution(jobs):
    
    cnt = len(jobs)
    
    heapify(jobs)
    
    waiting = []

    now_time = 0
    total_time = 0
    
    while waiting or jobs:
        # 현재 시작할 수 있는 작업을 다 넣음
        while jobs:
            if jobs[0][0] > now_time:
                break
            s, l = heappop(jobs)
            heappush(waiting, (l, s))
        
        # 근데 지금 아무것도 시작할 수 없다면? 제일 먼저 들어오는 요청시간으로 이동
        if not waiting:
            now_time = jobs[0][0]
            continue

        # 하나의 작업 실행
        running_time, start_time = heappop(waiting)
        now_time += running_time
        total_time += now_time - start_time

    return total_time//cnt