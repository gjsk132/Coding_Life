from collections import defaultdict
input = open(0).readline

cnt = int(input())

origin = list(map(int,input().split()))

num = sorted(set(origin))

num_dict = defaultdict(int)

for k, v in enumerate(num):
    num_dict[v] = k

for i in origin:
    print(num_dict[i], end=" ")