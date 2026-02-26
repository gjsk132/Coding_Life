cases = int(input())

for _ in range(cases):
    N, dist, train_1, train_2, fly = map(float, input().split())

    print(f"{int(N)} {fly*(dist/(train_1 + train_2)):.6f}")