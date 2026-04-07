import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)

# 아래, 아래 오른쪽, 오른쪽, 오른쪽 위, 위, 위 왼쪽, 왼쪽, 왼쪽 아래
dxs = [1, 1, 0, -1, -1, -1, 0, 1]
dys = [0, 1, 1, 1, 0, -1, -1, -1]

def in_range(x, y):
    return 0 <= x < h and 0 <= y < w

def dfs(x, y):
    visited[x][y] = True

    for dx, dy in zip(dxs, dys):
        nx, ny = x + dx, y + dy

        if not in_range(nx, ny):
            continue
        if grid[nx][ny] == 0:
            continue
        if visited[nx][ny]:
            continue

        dfs(nx, ny)


while True:
    w, h = map(int, input().split())

    if w == 0 and h == 0:
        break

    grid = [
        list(map(int, input().split()))
        for _ in range(h)
    ]
    visited = [
        [False] * w
        for _ in range(h)
    ]

    answer = 0
    for x in range(h):
        for y in range(w):
            if grid[x][y] == 1 and not visited[x][y]:
                dfs(x, y)
                answer += 1

    print(answer)