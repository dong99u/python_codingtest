import sys
input = sys.stdin.readline

n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

dp = [[0] * n for _ in range(n)]
dp[0][0] = grid[0][0]

for i in range(n):
    for j in range(n):
        if i == 0 and j == 0:
            continue
        if i == 0:
            dp[i][j] = max(dp[i][j - 1], grid[i][j])
        if j == 0:
            dp[i][j] = max(dp[i - 1][j], grid[i][j])
        if i > 0 and j > 0:
            dp[i][j] = max(min(dp[i - 1][j], dp[i][j - 1]), grid[i][j])

print(dp[n - 1][n - 1])
