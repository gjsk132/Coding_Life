from math import sqrt

is_prime = [True]*(10**7)
is_prime[0], is_prime[1] = False, False

for i in range(2, int(sqrt(10**7))+1):
    if is_prime[i]:
        for j in range(i+i, 10**7, i):
            is_prime[j] = False

def solution(numbers):
    
    check = [False]*len(numbers)
    
    
    
    def backtracking(s, cnt):
        ans = set([])
        
        if cnt > 0:
            if is_prime[int(s)]:
                ans.add(int(s))

        if cnt == len(numbers):
            return ans

        for i, n in enumerate(numbers):
            if not check[i]:
                check[i] = True
                ans = ans.union(backtracking(s + n, cnt+1))
                check[i] = False
        
        return ans
           
    answer = backtracking("", 0)
        
    return len(answer) if answer else 0