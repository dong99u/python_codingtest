import sys
from collections import deque
input = sys.stdin.readline

def in_range(x, y):
    return 0 <= x < n and 0 <= y < m

n, m = map(int, input().split())
grid = [list(map(int, list(input().rstrip()))) for _ in range(n)]

dist = [[0] * m for _ in range(n)]
dist[0][0] = 1

dxs = [1, 0, -1, 0]
dys = [0, 1, 0, -1]

q = deque([(0, 0)])

while q:
    x, y = q.popleft()
    for dx, dy in zip(dxs, dys):
        nx, ny = x + dx, y + dy

        if not in_range(nx, ny):
            continue
        if dist[nx][ny] != 0:
            continue
        if grid[nx][ny] != 1:
            continue

        dist[nx][ny] = dist[x][y] + 1
        q.append((nx, ny))

print(dist[-1][-1])