import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)

def dfs(v):
    visited[v] = True

    for nxt in graph[v]:
        if not visited[nxt]:
            dfs(nxt)

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
        dfs(v)
        answer += 1

print(answer)