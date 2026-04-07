import sys

input = sys.stdin.readline

N, M = map(int, input().rstrip().split()) # 5 3

nums = list(map(int, input().rstrip().split())) # 5 4 3 2 1
prefix_sum = [0] * (N + 1)

prefix_sum[1] = nums[0]
for i in range(2, N + 1):
    prefix_sum[i] = prefix_sum[i - 1] + nums[i - 1]

for _ in range(M):
    start, end = map(int, input().rstrip().split())

    print(prefix_sum[end] - prefix_sum[start - 1])

