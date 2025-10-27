def tracking():
    global n, m, perm, visited

    if len(perm) == m:
        print(*perm)
        return

    for num in range(1, n + 1, 1):
    # for i in range(idx, n , 1):
        if visited[num] == True:
            continue

        visited[num] = True
        perm.append(num)

        tracking()

        perm.pop()
        visited[num] = False

if __name__ == "__main__":
    import sys
    input = sys.stdin.readline

    n, m = map(int, input().split())

    perm = []
    visited = [False] * (n + 1)
    tracking()
    # tracking(0)
    # 1 2 / 1 3 / 1 4 / 2 3