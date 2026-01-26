input = open(0).readline

N, M = map(int, input().split())

target = list(reversed(list(map(int, input().split()))))

bq = list(range(1, N+1))

move_cnt = 0

def find_target(t, now):
    t_idx = now.index(t)
    t_len = len(now)

    now = now[t_idx+1:] + now[:t_idx]

    return min(t_idx, t_len-t_idx), now

while target:
    now_move_cnt, bq = find_target(target.pop(), bq)
    move_cnt += now_move_cnt

print(move_cnt)