input = open(0).readline

N, M = int(input()), int(input())

S = input().rstrip("O").lstrip("O")
S = S.replace("OI", "A")

answer = 0
cnt = 0
pos = 0

while pos < len(S):
    if S[pos] == "I":
        answer += max(0, cnt - N + 1)
        cnt = 0
    elif S[pos] == "O":
        answer += max(0, cnt - N + 1)
        cnt = -1
    elif S[pos] == "A":
        cnt += 1

    pos += 1

answer += max(0, cnt-N+1)

print(answer)