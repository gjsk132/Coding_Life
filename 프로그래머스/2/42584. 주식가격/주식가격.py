def solution(prices):
    
    answer = [-1 for _ in range(len(prices))]
    
    stack = []
    
    for idx, value in enumerate(prices):        
        
        while stack:
            if stack[-1][0] > value:
                _, i = stack.pop()
                answer[i] = idx - i
            else:
                break

        stack.append((value, idx))
    
    while stack:
        _, i = stack.pop()
        answer[i] = idx - i
    
    return answer