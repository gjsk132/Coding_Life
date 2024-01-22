num = int(input())
tree = list(reversed(sorted(map(int,input().split()))))
for i in range(num):
    tree[i] += i+2
print(max(tree))