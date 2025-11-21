input = open(0).readline

N, M = map(int, input().split())

gap = [0 for _ in range(100+1)]

n_dist, m_dist = 0, 0

for _ in range(N):
    load, limit = map(int, input().split())

    gap[n_dist:n_dist+load+1] = [-limit]*load

    n_dist += load

for _ in range(M):
    load, v = map(int, input().split())

    for _ in range(load):
        gap[m_dist] += v
        m_dist += 1

print(max(max(gap),0))