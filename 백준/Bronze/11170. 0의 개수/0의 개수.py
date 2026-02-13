input = open(0).readline

cases = int(input())

def find_zero(s, e):
    zero_count = 0

    for i in range(s, e+1):
        zero_count += str(i).count('0')
    
    return zero_count

for _ in range(cases):
    s, e = map(int, input().split())

    print(find_zero(s, e))