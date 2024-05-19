input = open(0).readline

while True:
    lotto = list(map(int,input().split()))

    if lotto.pop(0) == 0:
        break

    lotto.sort()
    comb = []

    def backtracking(cnt, last):
        if cnt == 6:
            print(*comb)
            return
        
        for num in lotto:
            if num < last or num in comb:
                continue
            comb.append(num)
            backtracking(cnt+1, num)
            comb.pop()

    backtracking(0, 0)
    print()