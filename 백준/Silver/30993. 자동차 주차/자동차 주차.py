input = open(0).readline

n, a, b, c  = map(int, input().split())

def combination(n, r):
    numerator = 1
    denominator = 1

    for i in range(r):
        numerator *= n - i
        denominator *= i + 1

    return numerator//denominator

print(combination(n, a) * combination(n-a, b))