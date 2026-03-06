def solution(sizes):
    max_length = max([max(s[0], s[1]) for s in sizes])
    
    other_length = 0
    
    for s in sizes:
        other_length = max(other_length, min(s))
    
    return max_length * other_length