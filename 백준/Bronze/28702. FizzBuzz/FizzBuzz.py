input = open(0).readline

target = 0
gap = 3

for _ in range(3):
    tmp = input().strip()

    try:
        tmp = int(tmp)
        target = gap + tmp
        break
    except:
        gap -= 1

answer = ""

if target%3 == 0:
    answer += "Fizz"
if target%5 == 0:
    answer += "Buzz"

print(target if answer == "" else answer)