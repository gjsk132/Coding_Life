N = int(input())

cnt = 0

def lowest_coprime(num):
    
    ans = 2

    def find_gcd(n, a):
        while n%a:
            n, a = a, n%a
        return a
    
    while not find_gcd(num, ans) == 1:
        ans += 1

    return ans

while not N == 2:
    N = lowest_coprime(N)
    cnt += 1

print("Soomin" if cnt%2 else "Song")