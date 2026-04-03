n, k = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]

prefix_sum = [[0] * (n + 1) for _ in range(n + 1)]

for i in range(1, n + 1):
    for j in range(1, n + 1):
        prefix_sum[i][j] = prefix_sum[i - 1][j] + prefix_sum[i][j - 1] + arr[i - 1][j - 1] - prefix_sum[i - 1][j - 1]

max_result = 0
for i in range(n - k + 1):
    for j in range(n - k + 1):
        x1, y1 = i, j
        x2, y2 = i + k - 1, j + k - 1
        max_result = max(max_result, prefix_sum[x2 + 1][y2 + 1] - prefix_sum[x1][y2 + 1] - prefix_sum[x2 + 1][y1] + prefix_sum[x1][y1])

print(max_result)