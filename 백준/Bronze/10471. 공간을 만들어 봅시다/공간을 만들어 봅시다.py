input = open(0).readline

room_sizes = set([])

total, partition = map(int, input().split())

p_poses = [0]+list(map(int, input().split()))+[total]

for s in range(len(p_poses)):
    for e in range(s, len(p_poses)):
        room_sizes.add(p_poses[e]-p_poses[s])        

print(" ".join(map(str, sorted(list(room_sizes))[1:])))