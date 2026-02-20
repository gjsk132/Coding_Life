from itertools import combinations

input = open(0).readline

heights = [int(input()) for _ in range(9)]

for combi in combinations(range(9), 7):
    if sum([heights[i] for i in combi]) == 100:
        for h in sorted([heights[i] for i in combi]):
            print(h)
        break