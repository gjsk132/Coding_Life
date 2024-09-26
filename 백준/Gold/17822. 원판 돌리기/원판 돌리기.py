import sys
sys.setrecursionlimit(100000)
input = open(0).readline

N, M, T = map(int, input().split())

target = [list(map(int,input().split())) for _ in range(N)]

offset = [(1, 0), (0,1), (-1,0), (0,-1)]

for _ in range(T):

    # 돌리기
    disk, dir, cnt = map(int,input().split())
    cnt = cnt if dir else M-cnt

    for i in range(disk, N+1, disk):
        target[i-1] = target[i-1][cnt:] + target[i-1][:cnt]

    # 인접 없애기
    
    def dfs(x, y, num):
        
        zero_cnt = 0

        for dx, dy in offset:

            nx = x + dx
            ny = (y + dy + M)%M
            
            if nx < 0 or nx == N:
                continue

            if target[nx][ny] == 0:
                continue

            if target[nx][ny] == num:
                
                if not target[x][y]:
                    zero_cnt += 1

                zero_cnt += 1
                target[x][y] = 0
                target[nx][ny] = 0
                zero_cnt += dfs(nx, ny, num)

        return zero_cnt


    zero_cnt = 0

    for i in range(N):

        for j in range(M):
            if not target[i][j] == 0:
                zero_cnt += dfs(i, j, target[i][j])
                
    # 인접 없을 시, 평균해서 값 변경하기
    if not zero_cnt:

        left_cnt = sum([sum([0 if j==0 else 1 for j in i])for i in target])
        
        if not left_cnt:
            break
        
        total = sum([sum(i) for i in target]) / left_cnt

        for k1, v1 in enumerate(target):
            for k2, v2 in enumerate(v1):
                if 0 < v2 < total:
                    target[k1][k2] += 1
                elif v2 > total:
                    target[k1][k2] -= 1

print(sum([sum(i) for i in target]))