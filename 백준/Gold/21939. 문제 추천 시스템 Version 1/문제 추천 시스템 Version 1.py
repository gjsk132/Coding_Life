from heapq import *

input = open(0).readline

max_hq = []
min_hq = []

prob_level = {}

def add(prob, level):
    heappush(max_hq, (-level, -prob))
    heappush(min_hq, (level, prob))
    prob_level[prob] = level

def solved(prob):
    prob_level[prob] = 0

def recommend(x):
    while True:
        level, prob = max_hq[0] if x == 1 else min_hq[0]

        if prob_level[abs(prob)] == abs(level):
            print(abs(prob))
            return
        else:
            heappop(max_hq if x==1 else min_hq)

for _ in range(int(input())):
    prob, level = map(int,input().split())

    add(prob, level)

for _ in range(int(input())):
    cmd = input().split()

    if cmd[0] == 'add':
        add(int(cmd[1]), int(cmd[2]))
    elif cmd[0] == 'solved':
        solved(int(cmd[1]))
    else:
        recommend(int(cmd[1]))