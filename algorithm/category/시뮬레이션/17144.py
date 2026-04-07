import sys
input = sys.stdin.readline

def in_range(x, y):
    return 0 <= x < r and 0 <= y < c

def spread():
    temp = [[0] * c for _ in range(r)]
    for x in range(r):
        for y in range(c):
            if grid[x][y] == 0:
                continue
            if grid[x][y] == -1:
                continue

            cnt = 0
            for dx, dy in zip(dxs, dys):
                nx, ny = x + dx, y + dy

                if not in_range(nx, ny):
                    continue
                if grid[nx][ny] == -1:
                    continue

                temp[nx][ny] += grid[x][y] // 5
                cnt += 1

            temp[x][y] -= (grid[x][y] // 5) * cnt

    for i in range(r):
        for j in range(c):
            grid[i][j] += temp[i][j]


def circular():

    for i in range(ventilate_row_idx - 1, 0, -1):
        grid[i][0] = grid[i - 1][0]
    for j in range(c - 1):
        grid[0][j] = grid[0][j + 1]
    for i in range(ventilate_row_idx):
        grid[i][-1] = grid[i + 1][-1]
    for j in range(c - 1, 1, -1):
        grid[ventilate_row_idx][j] = grid[ventilate_row_idx][j - 1]

    grid[ventilate_row_idx][1] = 0

    for i in range(ventilate_row_idx + 2, r - 1):
        grid[i][0] = grid[i + 1][0]
    for j in range(c - 1):
        grid[-1][j] = grid[-1][j + 1]
    for i in range(r - 1, ventilate_row_idx + 1, -1):
        grid[i][-1] = grid[i - 1][-1]
    for j in range(c - 1, 1, -1):
        grid[ventilate_row_idx + 1][j] = grid[ventilate_row_idx + 1][j - 1]

    grid[ventilate_row_idx + 1][1] = 0

r, c, t = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(r)]
ventilate_row_idx = 0 # 공기 청정기 맨 위쪽 row idx

# 공기 청정기의 맨 위쪽 row idx를 찾음
for i in range(r):
    if grid[i][0] == -1:
        ventilate_row_idx = i
        break

dxs = [1, 0, -1, 0]
dys = [0, 1, 0, -1]

for _ in range(t):
    spread()
    circular()

answer = 0
for i in range(r):
    for j in range(c):
        if grid[i][j] != -1:
            answer += grid[i][j]

print(answer)
