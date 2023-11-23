from collections import deque

input = open(0).readline
cnt = int(input())

deq = deque()

def is_empty(deque):
    if len(deque) == 0:
        return 1
    else: return 0

for i in range(cnt):
    cmdline = list(map(str, input().split()))
    cmd = cmdline[0]
    
    if cmd == 'push_front':
        deq.appendleft(int(cmdline[1]))\
        
    elif cmd == 'push_back':
        deq.append(int(cmdline[1]))
        
    elif cmd == 'pop_front':
        if is_empty(deq):
            print(-1)
        else:
            print(deq.popleft())
            
    elif cmd == 'pop_back':
        if is_empty(deq):
            print(-1)
        else:
            print(deq.pop())
            
    elif cmd == 'size':
        print(len(deq))
        
    elif cmd == 'empty':
        if is_empty(deq):
            print(1)
        else:
            print(0)
            
    elif cmd == 'front':
        if is_empty(deq):
            print(-1)
        else:
            print(deq[0])
        
    elif cmd == 'back':
        if is_empty(deq):
            print(-1)
        else:
            print(deq[-1])
        
    else: continue