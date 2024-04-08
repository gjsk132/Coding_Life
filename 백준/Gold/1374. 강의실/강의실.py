from heapq import *

input = open(0).readline

course_cnt = int(input())
course_time = []

for _ in range(course_cnt):
    idx, start, end = map(int,input().split())
    course_time.append((start, end))

course_time = sorted(course_time, key=lambda x:(x[0],x[1]))

end_time = []
max_cnt = 0

for start, end in course_time:
    while end_time and end_time[0] <= start:
        heappop(end_time)
    
    heappush(end_time, end)

    max_cnt = max(max_cnt, len(end_time))

print(max_cnt)