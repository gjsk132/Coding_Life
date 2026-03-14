from collections import defaultdict

input = open(0).readline

players = int(input())

round_check = {
    1 : defaultdict(int),
    2 : defaultdict(int),
    3 : defaultdict(int)
}

score_board = []

# 중복 체크
for _ in range(players):
    one, two, three = map(int, input().split())

    round_check[1][one] += 1
    round_check[2][two] += 1
    round_check[3][three] += 1

    score_board.append([one, two, three])

for one, two, three in score_board:
    total = one if round_check[1][one] == 1 else 0
    total += two if round_check[2][two] == 1 else 0
    total += three if round_check[3][three] == 1 else 0
    print(total)