input = open(0).readline

N = int(input())

words = [input().strip() for _ in range(N)]

words = list(set(words))

words.sort()
words.sort(key=len)

print("\n".join(words))