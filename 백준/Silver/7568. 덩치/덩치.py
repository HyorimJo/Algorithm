n = int(input())
w, h = [0] * n, [0] * n

for i in range(n):
    w[i], h[i] = map(int, input().split())

for i in range(n):
    rank = 1 # 일단 기본 등수는 1
    for j in range(n):
        if w[i] < w[j] and h[i] < h[j]: # 나보다 큰게 있으면 rank += 1
            rank += 1
    print(rank, end=' ')