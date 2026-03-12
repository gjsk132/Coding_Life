input = open(0).readline

N, M = map(int, input().split())

print("yaho" if M*100 >= N*81 else "no")