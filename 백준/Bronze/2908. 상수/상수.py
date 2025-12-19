input = open(0).readline

A, B = input().split()

A, B = A[::-1], B[::-1]

print(A if int(A) > int(B) else B)