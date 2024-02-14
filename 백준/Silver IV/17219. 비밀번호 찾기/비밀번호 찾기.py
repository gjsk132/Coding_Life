input = open(0).readline

site, pw = map(int,input().split())

pwDict = dict()

for i in range(site):
    s, p = map(str,input().split())
    pwDict[s] = p
    
for j in range(pw):
    print(pwDict[input().strip()])