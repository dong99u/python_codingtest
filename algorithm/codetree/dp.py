import sys
input = sys.stdin.readline

n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

dp = [[0] * m for _ in range(n)]
dp[0][0] = 1

for i in range(n):
    for j in range(m):
        for pi in range(i):        # 모든 윗행
            for pj in range(j):    # 모든 왼쪽열
                if grid[pi][pj] < grid[i][j] and dp[pi][pj] > 0:
                    dp[i][j] = max(dp[i][j], dp[pi][pj] + 1)

print(max(dp[i][j] for i in range(n) for j in range(m)))