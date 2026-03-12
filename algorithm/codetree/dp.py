import sys
input = sys.stdin.readline

INF = float('inf')

n, m = map(int, input().split())
A = list(map(int, input().split()))

dp = [INF] * (m + 1)
dp[0] = 0

for j in range(n):
    for i in range(m, -1, -1):
        if i >= A[j]:
            if dp[i - A[j]] == INF:
                continue

            dp[i] = min(dp[i], dp[i - A[j]] + 1)

print(dp[-1] if dp[-1] != INF else -1)