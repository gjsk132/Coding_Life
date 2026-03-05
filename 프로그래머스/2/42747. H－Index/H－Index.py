def solution(citations):
    
    citations.sort(reverse = True)
    
    # n편 : len(citations)
    # h번 이상 인용된 논문 h편
    # h번 이하 인용된 나머지 논문 (n-h)
    # h의 최댓값
    
    max_h = 0
    
    for i, c in enumerate(citations):
        if c >= i+1:
            max_h = i+1
    
    return max_h