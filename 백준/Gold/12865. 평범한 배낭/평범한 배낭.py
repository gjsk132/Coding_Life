input = open(0).readline

N, K = map(int, input().split())
objects = [map(int, input().split()) for _ in range(N)]

max_values = [0] * (K + 1)

for weight, value in objects:
    for max_load in range(K, -1, -1):
        if weight > max_load:
            break
        
        max_values[max_load] = max(max_values[max_load - weight] + value, max_values[max_load])
        
print(max_values[K])