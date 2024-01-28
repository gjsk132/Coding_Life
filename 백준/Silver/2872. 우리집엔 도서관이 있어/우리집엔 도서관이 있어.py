input = open(0).readline

n = int(input())
books = [int(input()) for i in range(n)]

now = books.index(n)
limit = max(books[now+1:] if now!=n-1 else [0])
result = limit

while now > 0 :
    if books[now] == n:
        n-= 1
    elif books[now] > limit:
        result += 1
    
    now -= 1
    
print(result)