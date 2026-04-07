import sys
from collections import deque
input = sys.stdin.readline

def in_range(x, y):
    return 0 <= x < n and 0 <= y < n

def find_start_point():
    for i in range(n):
        for j in range(n):
            if grid[i][j] == 9:
                return i, j

def bfs(x, y):
    dist = [[0] * n for _ in range(n)]
    visited = [[False] * n for _ in range(n)]
    q = deque([(x, y)])
    visited[x][y] = True

    fishes = []

    while q:
        x, y = q.popleft()

        for dx, dy in zip(dxs, dys):
            nx, ny = x + dx, y + dy

            if not in_range(nx, ny):
                continue
            if visited[nx][ny]:
                continue
            if size < grid[nx][ny]:
                continue

            dist[nx][ny] = dist[x][y] + 1
            visited[nx][ny] = True
            q.append((nx, ny))

            if 0 < grid[nx][ny] < size:
                fishes.append((dist[nx][ny], nx, ny))

    if not fishes:
        return False

    fishes.sort()
    d, x, y = fishes[0]

    return x, y, d

n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

# 상 좌 하 우
dxs = [-1, 0, 1, 0]
dys = [0, -1, 0, 1]

size = 2
cnt = 0
time = 0

x, y = find_start_point()

while True:
    result = bfs(x, y)
    if result == False:
        break
    else:
        grid[x][y] = 0
        nx, ny, dist = result
        time += dist
        grid[nx][ny] = 9
        cnt += 1
        if cnt == size:
            cnt = 0
            size += 1
        x, y = nx, ny

print(time)
