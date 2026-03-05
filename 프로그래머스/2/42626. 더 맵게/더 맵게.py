from heapq import *

def solution(scoville, K):
    
    heapify(scoville)
    
    mix_cnt = 0
    
    while len(scoville) > 1:
        if scoville[0] >= K:
            return mix_cnt
        
        a, b = heappop(scoville), heappop(scoville)
        heappush(scoville, a+b*2)
        mix_cnt += 1
    
    return mix_cnt if scoville[0] >= K else -1