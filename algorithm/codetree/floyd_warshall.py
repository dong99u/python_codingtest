dp = [
    [float('inf')] * 7
    for _ in range(7)
]

for i in range(1, 7):
    dp[i][i] = 0

edges = [
    (1, 2, 2),
    (1, 3, 5),
    (1, 4, 1),
    (2, 3, 3),
    (2, 4, 2),
    (3, 3, 4),
    (3, 5, 1),
    (3, 6, 5),
    (4, 5, 1),
    (5, 6, 2)
]

for u, v, w in edges:
    dp[u][v] = w
    dp[v][u] = w

for k in range(1, 7):
    for i in range(1, 7):
        for j in range(1, 7):

            if dp[i][k] + dp[k][j] < dp[i][j]:
                dp[i][j] = dp[i][k] + dp[k][j]

for row in dp:
    print(*row)