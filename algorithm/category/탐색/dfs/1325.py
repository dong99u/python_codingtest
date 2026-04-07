import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())

graph = [[] for _ in range(n + 1)]

for _ in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)

counts = [0] * (n + 1)

def bfs(v):
    visited = [False] * (n + 1)
    q = deque([v])
    visited[v] = True

    while q:
        now = q.popleft()
        for i in graph[now]:
            if not visited[i]:
                visited[i] = True
                counts[i] += 1
                q.append(i)

for i in range(1, n + 1):
    bfs(i)

max_val = max(counts)
for i in range(1, n + 1):
    if max_val == counts[i]:
        print(i, end=' ')