input = open(0).readline

num, cnt = map(int,input().split())

memo = [set(), set()]

memo[0].add(num)

for i in range(cnt):
    while memo[i%2]:
        
        n = list(str(memo[i%2].pop()))

        for p1 in range(len(n)):
            for p2 in range(p1):
                n[p1], n[p2] = n[p2], n[p1]
                memo[(i+1)%2].add(int("".join(n)))
                n[p1], n[p2] = n[p2], n[p1]

if memo[cnt%2]:
    answer = max(memo[cnt%2])
    print(answer if len(str(answer)) == len(str(num)) else -1)
else:
    print(-1)
