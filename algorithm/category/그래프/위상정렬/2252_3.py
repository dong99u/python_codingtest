import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]
D = [0] * (n + 1)

q = deque()

for _ in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)
    D[v] += 1

for i in range(1, n + 1):
    if D[i] == 0:
        q.append(i)

answer = []
while q:
    now = q.popleft()
    answer.append(now)
    for next in graph[now]:
        D[next] -= 1
        if D[next] == 0:
            q.append(next)

print(*answer)