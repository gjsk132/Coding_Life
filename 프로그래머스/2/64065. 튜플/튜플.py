from collections import defaultdict

def solution(s):
    cnt = defaultdict(int)
    for value in list(map(int, s.replace("{", "").replace("}", "").split(","))):
        cnt[value] += 1

    answer = sorted(cnt.items(), key=lambda x:-x[1])

    answer = [k for k, v in answer]

    return answer