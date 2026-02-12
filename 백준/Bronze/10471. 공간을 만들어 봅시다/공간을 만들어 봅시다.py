input = open(0).readline

room_sizes = set([])

total, partition = map(int, input().split())

p_poses = [0]+list(map(int, input().split()))+[total]

room_lens = [p_poses[i+1]-p_poses[i] for i in range(partition+1)]

for s in range(len(room_lens)):
    for e in range(s, len(room_lens)):
        room_sizes.add(sum(room_lens[s:e+1]))

print(" ".join(map(str, sorted(list(room_sizes)))))