import sys
input = sys.stdin.readline

N, M = map(int, input().split())
w, v = zip(*[tuple(map(int, input().split())) for _ in range(N)])
w, v = list(w), list(v)

dp = [0] * (M + 1)

for i in range(N):
    for j in range(M + 1):
        if w[i] <= j:
            dp[j] = max(dp[j], dp[j - w[i]] + v[i])

print(dp[M])