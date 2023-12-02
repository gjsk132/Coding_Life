from itertools import permutations
n, m = map(int, input().split())
for i in map(list, permutations(range(1, n+1), m)):
    print(*i)