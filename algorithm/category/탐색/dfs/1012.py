import sys
sys.setrecursionlimit(10000000)
input = sys.stdin.readline

t = int(input())

def in_range(x, y):
    return 0 <= x < m and 0 <= y < n

def dfs(x, y):
    dxs = [-1, 0, 1, 0]
    dys = [0, 1, 0, -1]

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

for _ in range(t):
    m, n, k = map(int, input().split())
    graph = [[0] * n for _ in range(m)]

    for _ in range(k):
        x, y = map(int, input().split())
        graph[x][y] = 1

    visited = [[False] * n for _ in range(m)]
    result = 0
    for x in range(m):
        for y in range(n):
            if graph[x][y] == 0 or visited[x][y]:
                continue

            dfs(x, y)
            result += 1

    print(result)