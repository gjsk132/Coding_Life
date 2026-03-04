def solution(s):
    answer = True
    
    cnt = 0
    
    for ss in s:
        if ss == '(':
            cnt += 1
        else:
            if cnt == 0:
                return False
            cnt -= 1

    return True if not cnt else False