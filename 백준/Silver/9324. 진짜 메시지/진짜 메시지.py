from collections import defaultdict

input = open(0).readline

def check_message(message):
    alpha_cnt = defaultdict(int)

    for idx, m in enumerate(list(message)):
        if alpha_cnt[m] == 3:
            alpha_cnt[m] = 0
            
            if not message[idx-1] == m:
                return False

        else:
            alpha_cnt[m] += 1

    return False if 3 in alpha_cnt.values() else True
        
cases = int(input())

for _ in range(cases):
    print("OK" if check_message(input().strip()) else "FAKE")