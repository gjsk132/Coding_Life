input = open(0).readline

def greatest_common_divisor(a, b):
    max_n, min_n = max(a, b), min(a, b)

    while min_n:
        max_n, min_n = min_n, max_n%min_n

    return max_n

cnt = int(input())
nums = list(map(int, input().split()))

std_num = int(input())

total_cnt = 0
total_sum = 0

for n in nums:
    if greatest_common_divisor(n, std_num) == 1:
        total_cnt += 1
        total_sum += n

print(total_sum/total_cnt)