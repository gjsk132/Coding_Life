from collections import defaultdict, deque

def solution(edges):
    
    grape = defaultdict(list)
    
    check = [True]*(max(map(max, edges))+1)
    check[0] = False
    
    for s, e in edges:
        grape[s].append(e)
        if check[e]:
            check[e] = False

    start = 1
    eight, stick, donut = 0, 0, 0
    
    # find start and eight loop ( 2 or more start node in line )
    for k, v in zip(grape.keys(), grape.values()):
        
        # 들어오는 간선이 있으면서, 길이가 2인 경우
        if len(v) == 2 and not check[k]:
            eight += 1
            
            edq = deque()
            edq.append(k)
            while edq:
                n = edq.popleft()
                if not check[n]:
                    check[n] = True
                    for i in grape[n]:
                        edq.append(i)
        # 길이가 가장 긴 것을 기억하고 있음. (위 조건문과는 완전 별개개)
        elif len(v) > start and check[k]:
            start = k

    # false node connected with top node(start)
    node = deque()
    for i in grape[start]:
        if check[i]:
            continue
        node.append(i)

    # find stick and just loop (meet True node after node check)
        
    while node:
        n = node.popleft()
        check[n] = True
    
        if not grape[n]:
            stick += 1
        else:
            for i in grape[n]:
                if check[i]:
                    donut += 1
                    break
                node.append(i)
                
    return [start, donut, stick, eight]