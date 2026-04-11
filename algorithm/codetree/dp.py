import sys; input = lambda: sys.stdin.readline().rstrip()

INF = sys.maxsize

n = int(input())
arr = [0] + list(map(int, input().split()))

dp = [[-INF] * 4 for _ in range(n + 1)]
dp[0][0] = 0
dp[1][1] = arr[1]

for i in range(2, n + 1):
    # 두 칸 전에서 점프
    for j in range(4):
        dp[i][j] = max(dp[i][j], dp[i - 2][j] + arr[i])

    # 한 칸 전에서 점프
    for j in range(1, 4):
        dp[i][j] = max(dp[i][j], dp[i - 1][j - 1] + arr[i])

print(max(dp[n]))