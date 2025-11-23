from collections import defaultdict

input = open(0).readline

def calculate_cases(clothes_cnt):
    clothes = defaultdict(int)

    for _ in range(clothes_cnt):
        c_name, c_sort = input().split()

        clothes[c_sort] += 1
    
    answer = 1
    
    for v in clothes.values():
        answer *= (v+1)

    return answer-1

cases = int(input())

for _ in range(cases):
    c_cnt = int(input())

    print(calculate_cases(c_cnt))