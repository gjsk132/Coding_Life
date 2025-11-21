input = open(0).readline

cases = int(input())

case_list = [int(input()) for _ in range(cases)]

m_case = max(max(case_list), 1)

board = [[0, 0] for _ in range(m_case+1)]
board[0], board[1] = [1, 0], [0, 1]

for idx in range(2, m_case+1):
    board[idx][0] = board[idx-1][0]+board[idx-2][0]
    board[idx][1] = board[idx-1][1]+board[idx-2][1]

for c in case_list:
    print(board[c][0], board[c][1])