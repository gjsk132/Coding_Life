n = int(input())

answer = 0

if n <= 2:
    print(1)
else:
    memo = [1]*n
    
    for i in range(2, n):
        memo[i] += sum(memo[:i-1])

    print(memo[-1])