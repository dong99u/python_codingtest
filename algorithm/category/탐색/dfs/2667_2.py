import sys
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

def in_range(x, y):
    return 0 <= x < n and 0 <= y < n

def dfs(x, y):
    cnt = 1
    visited[x][y] = True
    for dx, dy in zip(dxs, dys):
        nx, ny = x + dx, y + dy

        if not in_range(nx, ny):
            continue
        if grid[nx][ny] == 0:
            continue
        if visited[nx][ny]:
            continue

        cnt += dfs(nx, ny)

    return cnt

n = int(input())
grid = [list(map(int, list(input().rstrip()))) for _ in range(n)]
visited = [[False] * n for _ in range(n)]

dxs = [1, 0, -1, 0]
dys = [0, 1, 0, -1]

answers = []
for x in range(n):
    for y in range(n):
        if grid[x][y] == 1 and not visited[x][y]:
            cnt = dfs(x, y)
            answers.append(cnt)

answers.sort()
print(len(answers))
for num in answers:
    print(num)