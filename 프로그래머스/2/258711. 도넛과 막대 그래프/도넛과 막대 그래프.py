from collections import defaultdict, deque

def solution(edges):
    
    graph = defaultdict(set)
    
    check = [True]*(max(map(max, edges))+1)
    check[0] = False
    
    for s, e in edges:
        graph[s].add(e)
        if check[e]:
            check[e] = False

    start = 0
    total = 0
    eight, stick, donut = 0, 0, 0
    
    # find start and eight loop ( 2 or more start node in line )
    for k, v in zip(graph.keys(), graph.values()):
        if len(v) == 2 and not check[k]:
            eight += 1
            
            edq = deque()
            edq.append(k)
            while edq:
                n = edq.popleft()
                if not check[n]:
                    check[n] = True
                    for i in graph[n]:
                        edq.append(i)
        elif len(v) > total and check[k]:
            start = k
            total = len(v)

    # false node connected with top node(start)
    node = deque()
    for i in graph[start]:
        if check[i]:
            continue
        node.append(i)

    # find stick and just loop (meet True node after node check)
        
    while node:
        n = node.popleft()
        check[n] = True
    
        if graph[n]==set():
            stick += 1
            continue
            
        for i in graph[n]:
            if check[i]:
                donut += 1
                break
            node.append(i)
                
    return [start, donut, stick, eight]