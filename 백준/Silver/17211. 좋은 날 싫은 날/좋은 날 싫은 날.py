left_day, state = map(int, input().split())

good_good, good_bad, bad_good, bad_bad = map(float, input().split())

p_good, p_bad = 1 if not state else 0, 1 if state else 0

for _ in range(left_day):
    p_good, p_bad = p_good*good_good + p_bad*bad_good, p_good*good_bad + p_bad*bad_bad
    
print(int(p_good*1000+0.5))
print(int(p_bad*1000+0.5))