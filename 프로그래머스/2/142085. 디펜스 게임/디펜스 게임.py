from heapq import *
from collections import deque

def solution(n, k, enemy):
    round = 0

    fight = []

    for e in enemy:
        round += 1
        n -= e
        heappush(fight, -e)

        while n < 0 and k > 0:
            k -= 1
            n -= heappop(fight)
        
        if n < 0 :
            round -= 1
            break

    return round