import sys
sys.setrecursionlimit(100000000)
input = sys.stdin.readline

def in_range(x, y):
    return 0 <= x < h and 0 <= y < w

def dfs(x, y):
    dxs = [-1, -1, 0, 1, 1, 1, 0, -1]
    dys = [0, 1, 1, 1, 0, -1, -1, -1]

    visited[x][y] = True

    for dx, dy in zip(dxs, dys):
        nx, ny = x + dx, y + dy

        if not in_range(nx, ny):
            continue
        if graph[nx][ny] == 0:
            continue
        if visited[nx][ny]:
            continue

        dfs(nx, ny)


while True:
    w, h = map(int, input().split())

    if w == 0 and h == 0:
        break

    graph = [
        list(map(int, input().split()))
        for _ in range(h)
    ]

    visited = [[False] * w for _ in range(h)]
    result = 0
    for x in range(h):
        for y in range(w):
            if graph[x][y] == 0 or visited[x][y]:
                continue

            dfs(x, y)
            result += 1

    print(result)
