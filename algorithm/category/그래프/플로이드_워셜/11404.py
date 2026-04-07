import sys
input = sys.stdin.readline

INF = float('inf')
n = int(input())
m = int(input())

dp = [[INF] * (n + 1) for _ in range(n + 1)]

for i in range(n + 1):
    dp[0][i] = None
    dp[i][0] = None

for i in range(1, n + 1):
    dp[i][i] = 0

for _ in range(m):
    a, b, c = map(int, input().split())
    dp[a][b] = min(dp[a][b], c)


for k in range(1, n + 1):
    for u in range(1, n + 1):
        for v in range(1, n + 1):
            if dp[u][v] > dp[u][k] + dp[k][v]:
                dp[u][v] = dp[u][k] + dp[k][v]

for i in range(1, n + 1):
    for j in range(1, n + 1):
        if dp[i][j] == INF:
            print(0, end=' ')
        else:
            print(dp[i][j], end=' ')
    print()