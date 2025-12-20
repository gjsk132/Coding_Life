from collections import defaultdict

input = open(0).readline

a, b, c = map(int, input().split())

def divide_conquer(base, exponent):
    if exponent == 1:
        return base%c

    if exponent%2:
        return divide_conquer(base*base%c, exponent//2)*base%c
    else:
        return divide_conquer(base*base%c, exponent//2)

print(divide_conquer(a%c, b))