from collections import defaultdict

input = open(0).readline

point_cnt = int(input())

point_in_color = defaultdict(list)

for _ in range(point_cnt):
    pos, color = map(int, input().split())

    point_in_color[color].append(pos)

sum_of_arrow = 0

for same_color_poses in point_in_color.values():

    same_color_poses_cnt = len(same_color_poses)

    if same_color_poses_cnt == 1:
        continue

    same_color_poses.sort()

    for i in range(len(same_color_poses)):
        if i == 0:
            sum_of_arrow += same_color_poses[i+1] - same_color_poses[i]
        elif i == same_color_poses_cnt -1:
            sum_of_arrow += same_color_poses[i] - same_color_poses[i-1]
        else:
            sum_of_arrow += min(same_color_poses[i]-same_color_poses[i-1], same_color_poses[i+1]-same_color_poses[i])

print(sum_of_arrow)