import sys; input = lambda: sys.stdin.readline().rstrip()
from collections import deque

n, m = map(int, input().split())
edges = [tuple(map(int, input().split())) for _ in range(m)]

graph = [[] for _ in range(n + 1)]
D = [0] * (n + 1)
for u, v in edges:
    graph[u].append(v)
    D[v] += 1

q = deque()
for i in range(1, n + 1):
    if D[i] == 0:
        q.append(i)

answer = []
while q:
    curr = q.popleft()
    answer.append(curr)
    for nxt in graph[curr]:
        D[nxt] -= 1
        if D[nxt] == 0:
            q.append(nxt)

print(*answer)