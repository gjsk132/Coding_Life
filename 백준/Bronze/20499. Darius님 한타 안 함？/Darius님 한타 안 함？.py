input = open(0).readline

kill, death, assist = map(int, input().split("/"))

print("hasu" if kill+assist<death or death==0 else "gosu")