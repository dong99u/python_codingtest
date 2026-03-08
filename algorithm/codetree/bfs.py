from collections import deque

dxs = [1, 0, -1, 0]
dys = [0, 1, 0, -1]

def in_range(x, y):
    return 0 <= x < n and 0 <= y < n

def can_move(x, y, dist):
    return in_range(x, y) and grid[x][y] == 1 and dist[x][y] == -1

def bfs(q):
    dist = [[-1] * n for _ in range(n)]
    for x, y in q:
        dist[x][y] = 0

    while q:
        cx, cy = q.popleft()
        for dx, dy in zip(dxs, dys):
            nx, ny = cx + dx, cy + dy
            if can_move(nx, ny, dist):
                dist[nx][ny] = dist[cx][cy] + 1
                q.append((nx, ny))

    return dist


n, k = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

q = deque()
for i in range(n):
    for j in range(n):
        if grid[i][j] == 2:
            q.append((i, j))
dist = bfs(q)

for i in range(n):
    for j in range(n):
        if grid[i][j] == 1 and dist[i][j] == -1:
            dist[i][j] = -2

for row in dist:
    print(*row)