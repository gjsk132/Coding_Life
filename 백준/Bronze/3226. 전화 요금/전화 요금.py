input = open(0).readline

cases = int(input())

# 7 to 19, 19 to 7
total_calling_time = [0, 0]
calling_offset = [7*60, 19*60]

for _ in range(cases):
    start_time, calling_time = input().split()

    hour, minute = map(int, start_time.split(":"))
    calling_time = int(calling_time)

    start_minute = hour*60+minute
    end_minute = start_minute + calling_time

    # start before 7
    if start_minute < calling_offset[0]:
        # end before 7
        if end_minute <= calling_offset[0]:
            total_calling_time[1] += end_minute - start_minute
        # end after 7
        else:
            total_calling_time[1] += calling_offset[0] - start_minute
            total_calling_time[0] += end_minute - calling_offset[0]

    # start after 7 before 19
    elif start_minute < calling_offset[1]:
        # end before 19
        if end_minute <= calling_offset[1]:
            total_calling_time[0] += end_minute - start_minute
        # end after 19
        else:
            total_calling_time[0] += calling_offset[1] - start_minute
            total_calling_time[1] += end_minute - calling_offset[1]
    
    # start after 19
    else:
        total_calling_time[1] += end_minute - start_minute

print(total_calling_time[0]*10+total_calling_time[1]*5)