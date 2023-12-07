input = open(0).readline
member = int(input())

members = [list(input().split()) for _ in range(member)]

while len(members) != 1:
    now = members.pop(0)
    index = int(now[1])%len(members)-1
    if index==-1:
        index += len(members)
    members.pop(index)
    members = members[index:] + members[:index]
    
print(members.pop()[0])