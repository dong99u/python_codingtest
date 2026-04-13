import sys; input = lambda: sys.stdin.readline().rstrip()
from collections import deque, defaultdict

dxs = [1, 0, -1, 0]
dys = [0, 1, 0, -1]

def in_range(x, y):
    return 0 <= x < n and 0 <= y < n

def can_move(x, y, w):
    return in_range(x, y) and not any(grid[x][y:y + w])

# 좌측 하단의 좌표 기준
def get_length(x, y):
    width = 0
    height = 0
    num = grid[x][y]

    for i in range(x, -1, -1):
        if not in_range(i, y):
            break
        if grid[i][y] != num:
            break
        height += 1

    for j in range(y, n):
        if not in_range(x, j):
            break
        if grid[x][j] != num:
            break
        width += 1

    return width, height

def drop():
    visited = set()
    for x in range(n - 1, -1, -1):
        for y in range(n):
            if grid[x][y] == 0 or grid[x][y] in visited:
                continue
            num = grid[x][y]
            visited.add(num)
            width, height = get_length(x, y)
            cx, cy = x, y
            while True:
                nx, ny = cx + 1, cy
                if not can_move(nx, ny, width):
                    break
                cx, cy = nx, ny
            if x != cx: # 내려갈 수 있다면
                offset = abs(cx - x)
                pos = bfs(x, y)

                # 기존의 박스 제거
                for i, j in pos:
                    grid[i][j] = 0
                # 내려갈 수 있는 최대 깊이에 박스 옮기기
                for i, j in pos:
                    grid[i + offset][j] = num

# 박스 정보 리턴
def bfs(x, y):
    visited = [[False] * n for _ in range(n)]
    q = deque([(x, y)])
    visited[x][y] = True
    num = grid[x][y]
    result = [(x, y)]
    while q:
        cx, cy = q.popleft()
        for dx, dy in zip(dxs, dys):
            nx, ny = cx + dx, cy + dy
            if not in_range(nx, ny): continue
            if visited[nx][ny]: continue
            if grid[nx][ny] != num: continue
            q.append((nx, ny))
            visited[nx][ny] = True
            result.append((nx, ny))

    return result

# 택배 투입
def insert(k, h, w, c):
    c -= 1 # 0-indexed
    cx, cy = h - 1, c
    while True:
        nx, ny = cx + 1, cy
        # 이 택배가 다른 택배 바로 위에 있거나 맨 아래에 내려왔을 경우 스톱
        if not can_move(nx, ny, w):
            break
        cx, cy = nx, ny
    # 택배 그리기
    for i in range(cx, cx - h, -1):
        for j in range(cy, cy + w):
            grid[i][j] = k

def pop(d):
    dd = defaultdict(list)
    cant_pop_set = set()
    j_range = range(n) if d == 0 else range(n - 1, -1, -1)
    for i in range(n - 1, -1, -1):
        found = False
        for j in j_range:
            if grid[i][j] in dd or grid[i][j] in cant_pop_set:
                found = True
                continue
            if grid[i][j] != 0 and found:
                cant_pop_set.add(grid[i][j])
            if grid[i][j] != 0 and grid[i][j] not in cant_pop_set and \
                    grid[i][j] not in dd:
                dd[grid[i][j]] = bfs(i, j)
                found = True
    min_k = 101
    for k in dd:
        if k not in cant_pop_set:
            min_k = min(min_k, k)
    for x, y in dd[min_k]:
        grid[x][y] = 0
    return min_k

n, m = map(int, input().split())
grid = [[0] * n for _ in range(n)]

for _ in range(m):
    k, h, w, c = map(int, input().split())

    # 택배 투입
    insert(k, h, w, c)

answer = []
for _ in range(m // 2):
    answer.append(pop(0))
    drop()
    answer.append(pop(1))
    drop()

for ans in answer:
    print(ans)