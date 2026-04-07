import sys

input = sys.stdin.readline

N, M = map(int, input().split()) # 4 3

nums = []

for _ in range(N):
    nums.append(list(map(int, input().split())))

prefix_sum = [
    [0] * (N + 1)
    for _ in range(N + 1)
]

for i in range(1, N + 1):
    for j in range(1, N + 1):
        prefix_sum[i][j] = prefix_sum[i][j - 1] + prefix_sum[i - 1][j] - prefix_sum[i - 1][j - 1] + nums[i - 1][j - 1]

for _ in range(M):
    x1, y1, x2, y2 = map(int, input().split()) # 2 2 3 4

    print(prefix_sum[x2][y2] - prefix_sum[x1 - 1][y2] - prefix_sum[x2][y1 - 1] + prefix_sum[x1 - 1][y1 - 1])