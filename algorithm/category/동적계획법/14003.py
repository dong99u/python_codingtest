import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))

dp = [1] * n
paths = [[] for _ in range(n)]
paths[0] = [arr[0]]

for i in range(1, n):
    for j in range(i):
        if arr[i] > arr[j]:
            if dp[i] < dp[j] + 1:
                dp[i] = dp[j] + 1
                paths[i] = paths[j] + [arr[i]]

answer = max(dp)
answer_lst = []
for elem in paths:
    if len(elem) == answer:
        answer_lst = elem

print(answer)
print(*answer_lst)