input = open(0).readline

for _ in range(int(input())):
    times = sorted(list(input().split()))

    angle = []

    for idx, t in enumerate(times):
        hour, minute = map(int, t.split(":"))
        hour = (hour*60 + minute)%720
        minute *= 12
        
        angle.append([min(abs(hour-minute), 720-abs(hour-minute)), idx])
        
    angle.sort()
    print(times[angle[2][1]])