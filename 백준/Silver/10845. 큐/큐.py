import sys
deque = []
for i in range(int(sys.stdin.readline())):
    cmd = sys.stdin.readline().split()
    if cmd[0] == "push":
        deque.append(int(cmd[1]))
    elif cmd[0] == "pop":
        if deque == []:
            print(-1)
        else:
            print(deque.pop(0))
    elif cmd[0] == "size":
        print(len(deque))
    elif cmd[0] == "empty":
        if deque == []:
            print(1)
        else:
            print(0)
    elif cmd[0] == "front":
        if deque == []:
            print(-1)
        else:
            print(deque[0])
    else:
        if deque == []:
            print(-1)
        else:
            print(deque[-1])