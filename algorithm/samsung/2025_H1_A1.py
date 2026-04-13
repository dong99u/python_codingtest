import sys; input = lambda: sys.stdin.readline().rstrip()

N, Q = map(int, input().split())
grid = [[0] * N for _ in range(N)]

pos = [list(map(int, input().split())) for _ in range(Q)]

group_id = 1
for r1, c1, r2, c2 in pos:
    for x in range(r1, r2):
        for y in range(c1, c2):
            grid[x][y] = group_id

    
