import sys; input = lambda: sys.stdin.readline().rstrip()
from collections import defaultdict

dxs = [1, 0, -1, 0]
dys = [0, 1, 0, -1]

def in_range(x, y):
    return 0 <= x < N and 0 <= y < N

def is_separated(group_id):
    def dfs(x, y):
        group_set.remove((x, y))
        for dx, dy in zip(dxs, dys):
            nx, ny = x + dx, y + dy
            if not in_range(nx, ny): continue
            if (nx, ny) not in group_set: continue
            dfs(nx, ny)

    group_set = set(groups[group_id])
    dfs(*groups[group_id][0])
    if len(group_set) == 0:
        return False # 그룹이 분리됨
    else:
        return True

def remove_group_from_grid(group_id):
    for x, y in groups[group_id]:
        grid[x][y] = 0

def move_grid():
    new_grid = [[0] * N for _ in range(N)]
    new_groups = defaultdict(list)

    # 넓이 내림차순, 같으면 투입순서(gid) 오름차순
    sorted_gids = sorted(groups.keys(), key=lambda g: (-len(groups[g]), g))

    for gid in sorted_gids:
        cells = groups[gid]
        min_x = min(x for x, y in cells)
        min_y = min(y for x, y in cells)
        offsets = [(x - min_x, y - min_y) for x, y in cells]

        placed = False
        for bx in range(N):
            for by in range(N):
                # 모든 offset 셀이 범위 안 + 빈 칸인지 확인
                if all(
                    in_range(bx + dx, by + dy) and new_grid[bx + dx][by + dy] == 0
                    for dx, dy in offsets
                ):
                    # 배치
                    for dx, dy in offsets:
                        new_grid[bx + dx][by + dy] = gid
                    new_groups[gid] = [(bx + dx, by + dy) for dx, dy in offsets]
                    placed = True
                    break
            if placed:
                break
        # placed == False면 버림 (사라짐)

    return new_grid, new_groups

def calc_result():
    adj_paris = set()
    for x in range(N):
        for y in range(N):
            if grid[x][y] == 0:
                continue
            for dx, dy in zip(dxs, dys):
                nx, ny = x + dx, y + dy
                if not in_range(nx, ny): continue
                if grid[nx][ny] == 0: continue
                if grid[x][y] != grid[nx][ny]:
                    a, b = min(grid[x][y], grid[nx][ny]), max(grid[x][y], grid[nx][ny])
                    adj_paris.add((a, b))

    result = 0
    for a, b in adj_paris:
        result += len(groups[a]) * len(groups[b])
    return result

N, Q = map(int, input().split())

grid = [[0] * N for _ in range(N)]
groups = defaultdict(list)
group_id = 0

for _ in range(Q):
    r1, c1, r2, c2 = map(int, input().split())
    group_id += 1

    prev = set()
    for x in range(r1, r2):
        for y in range(c1, c2):
            if grid[x][y] != 0:
                prev.add(grid[x][y])
            grid[x][y] = group_id
            groups[group_id].append((x, y))

    for num in prev:
        groups[num] = [(x, y) for x, y in groups[num]
                       if not (r1 <= x < r2 and c1 <= y < c2)]

        if not groups[num]:
            del groups[num]
            continue

        if is_separated(num):
            remove_group_from_grid(num)
            del groups[num]

    grid, groups = move_grid()

    print(calc_result())


