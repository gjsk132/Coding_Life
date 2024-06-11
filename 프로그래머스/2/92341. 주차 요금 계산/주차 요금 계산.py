from collections import defaultdict
from math import ceil

def solution(fees, records):
    default_time, default_fee, unit_time, unit_fee = fees
    
    time_table = {}
    total_time = defaultdict(int)
    
    for record in records:
        time, car_number, inout = record.split()
        
        minute, second = map(int,time.split(":"))
        
        time = 60*minute+second
        
        if inout == "IN":
            time_table[car_number] = time
        else:
            total_time[car_number] += time - time_table[car_number]
            del time_table[car_number]
    
    for car_number, time in time_table.items():
        total_time[car_number] += (23*60+59) - time
    
    answer = []
    print(total_time)
    for i in sorted(total_time.keys()):
        answer.append(default_fee+ ceil(max(0, total_time[i]-default_time)/unit_time)*unit_fee)
    
    return answer