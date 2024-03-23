from heapq import *

def solution(k, n, reqs):
    # 상담 유형별 분리
    reqs_type = [[] for _ in range(k+1)]
    
    for start, care, care_type in reqs:
        reqs_type[care_type].append((start, care))
    
    # 상담 유형에 배치된 직원 수별 delay시간 기억
    max_care = 1 + n - k

    delay_meno = []
    delay_cnt = 0

    # 유형의 수 만큼 반복
    for customer_list in reqs_type[1:]:
        
        # 해당 유형에 아무도 없다면 바로 다음으로
        if customer_list == []:
            continue

        care_cnt = 1
        delay = 0
        delay_per_care = []
        
        # 최대로 상담원을 배치할 수 있을 때까지만 직원을 늘린다.
        while care_cnt <= max_care:
            
            # 직원이 상담 종료 시간을 저장하여 우선순위 큐 사용
            next_care = [0 for delay_per_care in range(care_cnt)]
            heapify(next_care)
            
            # 총 대기 시간
            delay = 0
            
            # 고객마다 기다리는 시간을 계산하여 delay에 넣어주고
            # 상담 직원의 상담 종료 시간 갱신
            for start, care in customer_list:
                nc = heappop(next_care)
                delay += max(0, nc-start)
                heappush(next_care, max(nc, start)+care)
            
            # 만약 대기 시간이 없다면
            # 더 이상 인원 수를 늘리는게 의미없기 때문에 종료한다.
            if delay == 0:
                break
            
            # delay 시간을 append하고 사람 수를 추가한다.
            delay_per_care.append(delay)
            care_cnt += 1
        
        # 각각 인원 수 변동으로 인해서 시간이 누적되지 않도록 차이를 빼준다.
        cnt = len(delay_per_care)
        for i in range(cnt):
            delay_meno.append(delay_per_care[i]-(0 if i+1 == cnt else delay_per_care[i+1]))
            delay_cnt += 1

    # 모든 유형에서 사람이 추가되면서 일어나는 대기 시간 변동이 다 저장되어 있음
    # 이를 정렬
    delay_meno.sort()
    
    # 리스트를 정렬한 후, 사람이 부족해서 들 수 밖에 없는 대기 시간의 합을 구한다.
    return sum(delay_meno[:delay_cnt-(n-k)])