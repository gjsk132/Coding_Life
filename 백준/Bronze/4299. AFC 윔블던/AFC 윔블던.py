plus, minus = map(int, input().split())

more = (plus+minus)//2
flag = (plus+minus)%2
less = plus - more

if plus < minus or flag:
    print(-1)
else:
    print(more, less)