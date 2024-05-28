input = open(0).readline

N, M = map(int, input().split())
r, c, d = map(int, input().split())
room = [list(map(int, input().split())) for _ in range(N)]
offset = ((-1, 0), (0, 1), (1, 0), (0, -1))


cnt = 0

while True:
    # 1
    if room[r][c] == 0:
        room[r][c] = 2
        cnt += 1
    
    is_clean = False

    # 3 (반시계로 회전)
    for turn in range(1, 5):
        dr, dc = offset[d-turn]
        nr, nc = r + dr, c + dc
        
        if nr < 0 or nr == N or nc < 0 or nc == M or room[nr][nc] != 0:
            continue

        r, c = nr, nc
        d = (d - turn + 4)%4
        is_clean = True
        break

    # 2 (뒤로 한칸)
    if not is_clean:
        dr, dc = offset[d-2]
        nr, nc = r + dr, c + dc

        if nr < 0 or nr == N or nc < 0 or nc == M or room[nr][nc] == 1:
            break
        
        r, c = nr, nc

print(cnt)