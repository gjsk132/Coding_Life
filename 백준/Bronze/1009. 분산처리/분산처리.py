input = open(0).readline

n = int(input())

last = {1:"1", 2:"2486", 3:"3971", 4:"46", 5:"5", 6:"6", 7:"7931", 8:"8426", 9:"91"}

def answer(a, b):

    a %= 10
    b -= 1

    if a == 0:
        print(10)
    else:
        print(last[a][b%len(last[a])])

for _ in range(n):
    a, b = map(int, input().split())
    
    answer(a, b)