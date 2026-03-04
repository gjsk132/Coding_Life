from collections import defaultdict

def solution(participant, completion):
    
    name_list = defaultdict(int)

    for p in participant:
        name_list[p] += 1
    
    for c in completion:
        name_list[c] -= 1
    
    for k, v in name_list.items():
        if v:
            return k