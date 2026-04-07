import sys
from collections import deque
input = sys.stdin.readline

def in_range(x, y):
    return 0 <= x < n and 0 <= y < m

n, m = map(int, input().split())

graph = [
    list(map(int, input().rstrip()))
    for _ in range(n)
]

count = [
    [0] * m
    for _ in range(n)
]

dxs = [1, 0, -1, 0]
dys = [0, 1, 0, -1]

q = deque()
q.append((0, 0))
count[0][0] = 1

while q:
    x, y = q.popleft()

    for dx, dy in zip(dxs, dys):
        nx = x + dx
        ny = y + dy

        if not in_range(nx, ny):
            continue
        if graph[nx][ny] == 0:
            continue
        if count[nx][ny] != 0:
            continue

        count[nx][ny] = count[x][y] + 1

        q.append((nx, ny))

print(count[n - 1][m - 1])