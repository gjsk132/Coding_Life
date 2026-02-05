from collections import defaultdict

input = open(0).readline

word_cnt = int(input())
check = defaultdict(bool)

answer = 0

def add_new_word(w):
    for sep in range(len(w)):
        check[w[sep:]+w[:sep]] = True
    return 1

for _ in range(word_cnt):
    word = input().strip()

    if not check[word]:
        answer += add_new_word(word)

print(answer)