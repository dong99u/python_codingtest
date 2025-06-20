import sys
input = sys.stdin.readline

n = int(input())

minutes = [int(i) for i in input().split()]
minutes.sort()

dp = [0] * n
dp[0] = minutes[0]
for i in range(1, n):
    dp[i] = dp[i - 1] + minutes[i]

print(sum(dp))