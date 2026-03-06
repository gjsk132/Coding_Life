def solution(answers):
    
    ans1, ans2, ans3 = 0, 0, 0
    
    offset2 = [1, 3, 4, 5]
    offset3 = [3, 1, 2, 4, 5]
    
    for i, a in enumerate(answers):
        
        # ans1
        if (i%5)+1 == a:
            ans1 += 1
        
        # ans2
        if not i%2:
            ans2 += 1 if a == 2 else 0
            
        else:
            ans2 += 1 if offset2[(i//2)%4] == a else 0
        
        # ans3
        ans3 += 1 if offset3[(i//2)%5] == a else 0
        
    max_collect = max(ans1, ans2, ans3)
    
    answer = []
    
    if ans1 == max_collect:
        answer.append(1)
    if ans2 == max_collect:
        answer.append(2)
    if ans3 == max_collect:
        answer.append(3)
    
    return answer