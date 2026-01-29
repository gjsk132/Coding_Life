input = open(0).readline

n = int(input())

scores = [int(input()) for _ in range(n)]
first = scores[0]

if min(scores) == first:
    print("ez")
elif max(scores) == first:
    print("hard")
else:
    print("?")