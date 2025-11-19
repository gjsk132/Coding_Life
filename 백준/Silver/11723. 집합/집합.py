input = open(0).readline

S = 0

M = int(input())

for _ in range(M):
    command = list(map(str, input().split()))

    order = command[0]

    if order == "add":
        n = int(command[1])
        S |= (1<<n)

    elif order == "remove":
        n = int(command[1])
        S &= ~(1<<n)
    
    elif order == "check":
        n = int(command[1])
        print(1 if S&(1<<n) else 0)

    elif order == "toggle":
        n = int(command[1])
        S ^= (1<<n)

    elif order == "all":
        S |= 0b111111111111111111110

    elif order == "empty":
        S &= 0b0