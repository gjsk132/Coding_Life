from heapq import *

def solution(k, n, reqs):
    reqs_type = [[] for _ in range(k+1)]
    
    for start, care, care_type in reqs:
        reqs_type[care_type].append((start, care))
        
    max_care = 1 + n - k

    delay_meno = []
    delay_cnt = 0

    for customer_list in reqs_type[1:]:

        if customer_list == []:
            continue

        care_cnt = 1
        delay = 0
        delay_per_care = []

        while care_cnt <= max_care:

            next_care = [0 for delay_per_care in range(care_cnt)]
            heapify(next_care)

            delay = 0

            for start, care in customer_list:
                nc = heappop(next_care)
                delay += max(0, nc-start)
                heappush(next_care, max(nc, start)+care)

            if delay == 0:
                break

            delay_per_care.append(delay)
            care_cnt += 1

        for i in range(len(delay_per_care)):
            delay_meno.append(delay_per_care[i]-(0 if i+1 == len(delay_per_care) else delay_per_care[i+1]))
            delay_cnt += 1

    delay_meno.sort()
    return sum(delay_meno[:delay_cnt-(n-k)])