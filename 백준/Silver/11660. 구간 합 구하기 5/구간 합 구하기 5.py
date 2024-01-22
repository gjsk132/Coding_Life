input = open(0).readline

size, order = map(int,input().split())

table = [[0]*(size+1)]+[[0]+list(map(int,input().split())) for i in range(size)]

# 누적 합 구하기
for i in range(size):
    
    # row에서 누적 합
    for j in range(size):
        table[i+1][j+1] += table[i+1][j]
    # row x col 누적 합
    for j in range(size):
        table[i+1][j+1] += table[i][j+1]

# 결과 출력
for i in range(order):
    x1, y1, x2, y2 = map(int,input().split())
    print(table[x2][y2]+table[x1-1][y1-1]-table[x2][y1-1]-table[x1-1][y2])