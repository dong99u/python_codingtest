import sys
input = sys.stdin.readline

def dfs(v):
    visited[v] = True
    for next in graph[v]:
        if not visited[next]:
            answer[next] = v
            dfs(next)

n = int(input())
graph = [[] for _ in range(n + 1)]
visited = [False] * (n + 1)

for _ in range(n - 1):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

answer = [0] * (n + 1)

dfs(1)

for i in range(2, n + 1):
    print(answer[i])