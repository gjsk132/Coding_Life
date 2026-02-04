input = open(0).readline

limit = input().strip().count('a')
request = input().strip().count('a')

print("no" if request > limit else "go")