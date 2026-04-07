import sys
from collections import deque
input = sys.stdin.readline

def in_range(x, y):
    return 0 <= x < n and 0 <= y < m

def bfs():
    q = deque()

    for i in range(n):
        for j in range(m):
            if graph[i][j] == 1:
                q.append((i, j, 0))

    dxs = [0, 1, 0, -1]
    dys = [1, 0, -1, 0]

    answer = 0
    while q:
        x, y, day = q.popleft()
        answer = max(answer, day)

        for dx, dy in zip(dxs, dys):
            nx, ny = x + dx, y + dy

            if not in_range(nx, ny):
                continue
            if graph[nx][ny] != 0:
                continue

            graph[nx][ny] = 1
            q.append((nx, ny, day + 1))

    for row in graph:
        if 0 in row:
            return -1

    return answer


m, n = map(int, input().split())

graph = [
    list(map(int, input().split()))
    for _ in range(n)
]

print(bfs())