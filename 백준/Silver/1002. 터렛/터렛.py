input = open(0).readline

def count_intersections():
    x1, y1, r1, x2, y2, r2 = map(int, input().split())

    ctr_dist = pow(pow(x1-x2, 2) + pow(y1-y2, 2), 1/2)
    
    if x1 == x2 and y1 == y2 and r1 == r2:
        return (-1 if r1 !=0 else 1)
    elif ctr_dist > r1 + r2 or ctr_dist + min(r1, r2) < max(r1, r2):
        return 0
    elif ctr_dist == r1 + r2 or ctr_dist + min(r1, r2) == max(r1, r2):
        return 1
    else:
        return 2
    
for _ in range(int(input())):
    print(count_intersections())