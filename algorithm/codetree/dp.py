n = int(input())

dp = [-1] * (n + 1)
dp[0] = 1
dp[1] = 1

# 노드의 총 개수
for i in range(2, n + 1):
    sum_val = 0
    # j = 루트 노드의 값
    for j in range(1, i + 1):
        sum_val += dp[j - 1] * dp[i - j]
    dp[i] = sum_val

print(dp[n])