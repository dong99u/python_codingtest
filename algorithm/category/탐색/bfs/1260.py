from collections import deque
import sys
sys.setrecursionlimit(10000)
input = sys.stdin.readline

result_dfs = []

def dfs(v):
    visited[v] = True
    result_dfs.append(v)
    for i in graph[v]:
        if not visited[i]:
            dfs(i)

n, m, v = map(int, input().split())

graph = [[] for _ in range(n + 1)]

for _ in range(m):
    s, e = map(int, input().split())
    graph[s].append(e)
    graph[e].append(s)

for i in range(1, n + 1):
    graph[i].sort()

visited = [False] * (n + 1)

dfs(v)

q = deque()
visited = [False] * (n + 1)

result_bfs = []

q.append(v)
visited[v] = True

while q:
    here = q.popleft()
    result_bfs.append(here)

    for i in graph[here]:
        if not visited[i]:
            visited[i] = True
            q.append(i)

for num in result_dfs:
    print(num, end=' ')
print()
for num in result_bfs:
    print(num, end=' ')