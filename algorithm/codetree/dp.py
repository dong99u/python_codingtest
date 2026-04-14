import sys; input = lambda: sys.stdin.readline().rstrip()

n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

dp = [[-1] * (n + 1) for _ in range(n + 1)]
dp[0][0] = 0

for i in range(n):
    for j in range(n):
        if dp[i][j] == -1:
            continue

        # 카드 버리기 (같을 때 대결도 동일)
        dp[i + 1][j + 1] = max(dp[i + 1][j + 1], dp[i][j])

        # 상대 카드가 더 작은 경우 → 상대 카드 버려짐
        if a[i] < b[j]:
            dp[i + 1][j] = max(dp[i + 1][j], dp[i][j])

        # 남우 카드가 더 작은 경우 → 남우 점수 획득
        if a[i] > b[j]:
            dp[i][j + 1] = max(dp[i][j + 1], dp[i][j] + b[j])

ans = 0
for i in range(n + 1):
    ans = max(ans, dp[i][n], dp[n][i])

print(ans)