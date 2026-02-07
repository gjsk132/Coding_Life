input = open(0).readline

goal, least, limit, train, rest = map(int, input().split())

train_cnt = 0
time = 0

bpm = least

if limit-least < train:
    print(-1)
else:
    while not train_cnt == goal:
        if bpm + train > limit:
            bpm = max(least, bpm-rest)
        else:
            bpm += train
            train_cnt += 1
        time += 1

    print(time)