import sys
input = sys.stdin.readline

INF = float('inf')

n = int(input())
arr = list(map(int, input().split()))
total_sum = sum(arr)

dp = [-1] * (total_sum + 1)
dp[0] = 0

for i in range(n):
    for j in range(total_sum, 0, -1):
        if dp[j - arr[i]] != -1:
            dp[j] = dp[j - arr[i]] + 1

answer = 0

for i in range(total_sum + 1):
    if dp[i] >= 2:
        answer = max(answer, dp[i])

print(answer)