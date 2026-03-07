def solution(n, times):
    
    maximum = (max(times)*n)//len(times)
    
    def bineary_search(s, e):
        # 탈출
        if s > e:
            return s
    
        # 값 구하기
        
        mid = (s+e)//2
        
        checked = sum([mid//t for t in times])
        
        if checked < n:
            return bineary_search(mid+1, e)
        elif checked >= n:
            return bineary_search(s, mid-1)
    
    return bineary_search(1, maximum)