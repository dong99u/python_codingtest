import sys
input = sys.stdin.readline

def dfs(v):
    cnt = 1
    visited[v] = True
    for next in graph[v]:
        if not visited[next]:
            cnt += dfs(next)
    return cnt

n = int(input())
m = int(input())

graph = [[] for _ in range(n + 1)]
visited = [False] * (n + 1)

for _ in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

answer = dfs(1)

print(answer - 1)