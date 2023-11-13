input = open(0).readline

cnt = 0

n, p = map(int,input().split())

melody = [[] for i in range(7)]

for i in range(n):
    num, flat = map(int, input().split())
    if melody[num] == []:
        melody[num].append(flat)
        cnt += 1
    else:
        while True:
            if not melody[num] or melody[num][-1] < flat:
                melody[num].append(flat)
                cnt += 1
                break;
            elif melody[num][-1] == flat:
                break;
            else:
                del melody[num][-1]
                cnt += 1

print(cnt)