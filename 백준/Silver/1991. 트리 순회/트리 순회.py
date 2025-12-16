input = open(0).readline

bineary_tree = {}

node = int(input())

for _ in range(node):
    root, left, right = input().split()
    bineary_tree[root] = [left, right]

def preoder_traversal(n):
    if n == ".":
        return
    
    left, right = bineary_tree[n]

    print(n, end="")
    preoder_traversal(left)
    preoder_traversal(right)

def inorder_traversal(n):
    if n == ".":
        return
    
    left, right = bineary_tree[n]

    inorder_traversal(left)
    print(n, end="")
    inorder_traversal(right)

def postorder_traversal(n):
    if n == ".":
        return
    
    left, right = bineary_tree[n]

    postorder_traversal(left)
    postorder_traversal(right)
    print(n, end="")


preoder_traversal("A")
print()
inorder_traversal("A")
print()
postorder_traversal("A")