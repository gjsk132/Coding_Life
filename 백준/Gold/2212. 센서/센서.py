input = open(0).readline

node = int(input())
senser = int(input())

node_info = sorted(map(int,input().split()))
gap_info = sorted([node_info[i+1]-node_info[i] for i in range(node-1)])

print(sum(gap_info[:node-senser]))