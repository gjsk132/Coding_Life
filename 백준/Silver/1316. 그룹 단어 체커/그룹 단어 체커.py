from collections import defaultdict

input = open(0).readline

answer = 0

words = int(input())

def group_checker(w):
    alpha = defaultdict(bool)

    now = ""

    for a in list(w):
        if a == now:
            continue
        else:
            if alpha[a]:
                return False
            alpha[a] = True

            now = a

    return True

for _ in range(words):
    if group_checker(input().strip()):
        answer += 1

print(answer)