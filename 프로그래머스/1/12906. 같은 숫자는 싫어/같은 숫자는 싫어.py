def solution(arr):
    answer = [arr[0]]
    top = 0
    for a in arr[1:]:
        if a == answer[top]:
            continue
        answer.append(a)
        top += 1
    
    return answer