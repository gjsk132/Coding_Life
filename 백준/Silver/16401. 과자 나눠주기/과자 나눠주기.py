input = open(0).readline

people, snacks = map(int, input().split())

snack = sorted(list(map(int, input().split())))
snack = snack[max(0,snacks-people):]

start = 1
end = snack[-1]

while start <= end:
    mid = (start + end)//2
    give_people = 0

    for s in snack:
        give_people += s//mid
    if give_people >= people:
        start = mid + 1
    else:
        end = mid - 1
    
print(end)