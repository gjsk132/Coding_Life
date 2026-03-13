input = open(0).readline

while(True):
    n, m = map(int, input().split())
    if (not (total := n+ m)):
        break
    else:
        print(total)