def solution(name):

    length = len(name)

    index = [i for i in range(length) if name[i] != 'A']
    
    if not index:
        return 0
    
    move = min(length-index[0], index[-1])

    for k, v in enumerate(index[1:]):
        move = min(move, length-v+index[k]+min(length-v,index[k]))

    answer = sum([min(ord(i)-65, 91-ord(i)) for i in name]) + move

    print(answer)
    
    return answer