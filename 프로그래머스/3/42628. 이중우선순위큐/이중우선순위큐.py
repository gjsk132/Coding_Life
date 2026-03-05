from heapq import *
from collections import defaultdict

def solution(operations):
    check_num = defaultdict(int)
    
    max_heap = [] 
    min_heap = []
    
    for o in operations:
        order, value = o.split()
        
        if order == 'I':
            value = int(value)
            heappush(max_heap, -value)
            heappush(min_heap, value)
            check_num[value] += 1

        elif order == 'D':
            # 최소 제거
            if value == "-1":
                while min_heap:
                    if not check_num[min_heap[0]]:
                        heappop(min_heap)
                        continue
                    else:
                        check_num[heappop(min_heap)] -= 1
                        break
                
            # 최대 제거
            else:
                while max_heap:
                    if not check_num[-max_heap[0]]:
                        heappop(max_heap)
                        continue
                    else:
                        check_num[-heappop(max_heap)] -= 1
                        break
        
    # 제거된 숫자 삭제
    while min_heap:
        if not check_num[min_heap[0]]:
            heappop(min_heap)
            continue
        else:
            break
    while max_heap:
        if not check_num[-max_heap[0]]:
            heappop(max_heap)
            continue
        else:
            break
    
    return [-max_heap[0] if max_heap else 0, min_heap[0] if min_heap else 0]