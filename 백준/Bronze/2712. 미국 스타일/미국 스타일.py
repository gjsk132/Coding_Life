input = open(0).readline

cases = int(input())

offset = {
    "kg" : ("lb", 2.2046),
    "lb" : ("kg", 0.4536),
    "l" : ("g", 0.2642),
    "g" : ("l", 3.7854)
}

for _ in range(cases):
    amount, unit = input().split()
    
    print(f"{offset[unit][1]*float(amount):.4f} {offset[unit][0]}")