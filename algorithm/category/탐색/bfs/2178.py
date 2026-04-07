import sys
from collections import deque
input = sys.stdin.readline

def in_range(x, y):
    return 0 <= x < n and 0 <= y < m

q = deque()

n, m = map(int, input().split())
graph = [
    list(map(int, input().rstrip()))
    for _ in range(n)
]

result = [[0] * m for _ in range(n)]
result[0][0] = 1

dxs = [-1, 0, 1, 0]
dys = [0, 1, 0, -1]

q.append((0, 0))

while q:
    x, y = q.popleft()
    for dx, dy in zip(dxs, dys):
        nx, ny = x + dx, y + dy

        if not in_range(nx, ny):
            continue
        if graph[nx][ny] == 0:
            continue
        if result[nx][ny] != 0:
            continue

        result[nx][ny] = result[x][y] + 1
        q.append((nx, ny))

print(result[n - 1][m - 1])
