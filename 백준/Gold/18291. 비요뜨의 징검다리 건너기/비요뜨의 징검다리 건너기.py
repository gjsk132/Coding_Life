input = open(0).readline
limit = pow(10, 9) + 7

for tc in range(int(input())):
    print( 1 if (n:=int(input())) == 1 else pow(2, n-2, limit))