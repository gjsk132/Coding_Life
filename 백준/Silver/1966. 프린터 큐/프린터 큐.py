from collections import deque

input = open(0).readline

test = int(input())

for i in range(test):
    docus, target = map(int, input().split())
    
    docuslist = list(map(int,input().split()))
    
    deq = deque([])
    
    for k, v in enumerate(docuslist):
        deq.append([v,k]) #max 함수 사용할 때 중요도를 기준으로 먼저 나올 수 있게하기 위함.
    
    cnt = 1
    while True:
        high = max(deq)[0]
        
        docu = deq.popleft()
        
        if docu[0] < high:
            deq.append(docu)
        elif docu[1] == target:
            print(cnt)
            break
        else:
            cnt+=1