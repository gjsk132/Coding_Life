input = open(0).readline

resistance = ["black", "brown", "red", "orange", "yellow", "green", "blue", "violet", "grey", "white"]

answer = 0

answer += resistance.index(input().strip())*10 + resistance.index(input().strip())

answer = answer * pow(10, resistance.index(input().strip()))

print(answer)