import sys
from collections import deque
input = sys.stdin.readline

n, m, s = map(int, input().split())
graph = [[] for _ in range(n + 1)]

def dfs(v):
    dfs_visited[v] = True
    dfs_answer.append(v)
    for next in sorted(graph[v]):
        if not dfs_visited[next]:
            dfs(next)

for _ in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

dfs_visited = [False] * (n + 1)
dfs_answer = []
dfs(s)

bfs_visited = [False] * (n + 1)
bfs_answer = []

q = deque([s])
bfs_visited[s] = True
bfs_answer.append(s)

while q:
    now = q.popleft()
    for next in sorted(graph[now]):
        if not bfs_visited[next]:
            bfs_visited[next] = True
            q.append(next)
            bfs_answer.append(next)

for num in dfs_answer:
    print(num, end=' ')
print()
for num in bfs_answer:
    print(num, end=' ')


