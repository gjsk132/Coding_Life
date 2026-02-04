input = open(0).readline

def decrypt(y, z, n):
    return chr((ord(y)+ord(z)-(194+n))%26+97)

key = int(input())
words = list(input().split())

for w in words:
    cnt = len(w)//2

    for i in range(cnt):
        print(decrypt(w[2*i], w[2*i+1], key), end="")
    
    print(end=" ")