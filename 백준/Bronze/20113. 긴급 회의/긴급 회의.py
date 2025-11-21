input = open(0).readline

n = int(input())

vote_state = [0 for _ in range(n+1)]

for v in map(int, input().split()):
    if v != 0:
        vote_state[v] += 1

max_vote = max(vote_state)

if vote_state.count(max_vote) != 1:
    print("skipped")
else:
    print(vote_state.index(max_vote))