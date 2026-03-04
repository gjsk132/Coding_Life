from collections import defaultdict

def solution(clothes):
    
    clothes_list = defaultdict(int)
    
    for name, kinds in clothes:
        clothes_list[kinds] += 1
    
    answer = 1
    
    for cnt in clothes_list.values():
        answer *= cnt + 1
    
    return answer - 1