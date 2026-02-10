input = open(0).readline

cnt = int(input())
times = list(map(int, input().split()))

y_fee = sum([((i//30)+1)*10 for i in times])
m_fee = sum([((i//60)+1)*15 for i in times])

if m_fee > y_fee:
    print(f"Y {y_fee}")
elif m_fee < y_fee:
    print(f"M {m_fee}")
else:
    print(f"Y M {y_fee}")