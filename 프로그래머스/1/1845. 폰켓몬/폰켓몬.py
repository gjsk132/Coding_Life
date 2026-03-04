def solution(nums):
    
    nums_kind = list(set(nums))
    
    can_bring_cnt = len(nums)//2
    
    return min(len(nums_kind), can_bring_cnt)