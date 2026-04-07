import sys
from collections import deque
input = sys.stdin.readline

n, l = map(int, input().split())
arr = list(map(int, input().split()))

q = deque()

answer = []

for i in range(n):
    while q and q[-1][0] > arr[i]:
        q.pop()
    q.append((arr[i], i))
    if q[0][1] < i - l + 1:
        q.popleft()

    answer.append(q[0][0])

print(' '.join(map(str, answer)))

