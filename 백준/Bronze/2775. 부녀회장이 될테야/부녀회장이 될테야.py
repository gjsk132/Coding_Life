input = open(0).readline

memo = [[i for i in range(15)] for _ in range(15)]

for x in range(1, 15):
    for y in range(1, 15):
        memo[x][y] = memo[x-1][y] + memo[x][y-1]
        
for i in range(int(input())):
    print(memo[int(input())][int(input())])