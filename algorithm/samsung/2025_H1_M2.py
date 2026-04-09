import sys; input = lambda: sys.stdin.readline().rstrip()
import heapq

dxs = [1, 0, -1, 0]
dys = [0, 1, 0, -1]
INF = 1e9

def in_range(x, y):
    return 0 <= x < n and 0 <= y < n

def is_valid(cx, cy, dx, dy, k):
    for step in range(1, k + 1):
        mx, my = cx + dx * step, cy + dy * step
        if grid[mx][my] == '#': return False
    # 도착지 S 체크
    ex, ey = cx + dx * k, cy + dy * k
    if grid[ex][ey] == 'S': return False
    return True

def dijkstra(x1, y1, x2, y2):
    hq = [(0, x1, y1, 1)]
    costs = [[[INF] * 6 for _ in range(n)] for _ in range(n)]
    costs[x1][y1][1] = 0

    while hq:
        curr_cost, cx, cy, k = heapq.heappop(hq)

        if cx == x2 and cy == y2:
            return curr_cost

        if curr_cost > costs[cx][cy][k]:
            continue

        for dx, dy in zip(dxs, dys):
            nx, ny = cx + dx * k, cy + dy * k
            if not in_range(nx, ny):
                continue
            if not is_valid(cx, cy, dx, dy, k):
                continue

            new_cost = curr_cost + 1

            if new_cost < costs[nx][ny][k]:
                costs[nx][ny][k] = new_cost
                heapq.heappush(hq, (new_cost, nx, ny, k))

        # 점프력 증가
        if k < 5:
            new_cost = curr_cost + (k + 1) ** 2
            if new_cost < costs[cx][cy][k + 1]:
                costs[cx][cy][k + 1] = new_cost
                heapq.heappush(hq, (new_cost, cx, cy, k + 1))

        # 점프력 감소
        if k > 1:
            for i in range(k - 1, 0, -1):
                new_cost = curr_cost + 1
                if new_cost < costs[cx][cy][i]:
                    costs[cx][cy][i] = new_cost
                    heapq.heappush(hq, (curr_cost + 1, cx, cy, i))

    return min(costs[x2][y2])

n = int(input())
grid = [list(input()) for _ in range(n)]

Q = int(input())
pos = [list(map(int, input().split())) for _ in range(Q)]

for r1, c1, r2, c2 in pos:
    result = dijkstra(r1 - 1, c1 - 1, r2 - 1, c2 - 1)
    if result == INF:
        print(-1)
    else:
        print(result)



