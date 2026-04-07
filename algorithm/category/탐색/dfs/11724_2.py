import sys
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

def dfs(now):
    visited[now] = True
    for next in graph[now]:
        if not visited[next]:
            dfs(next)

n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]
visited = [False] * (n + 1)

for _ in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

answer = 0
for v in range(1, n + 1):
    if not visited[v]:
        answer += 1
        dfs(v)

print(answer)