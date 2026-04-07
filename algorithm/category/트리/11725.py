import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)

n = int(input())

def dfs(v):
    visited[v] = True
    for now in graph[v]:
        if not visited[now]:
            answer[now] = v
            dfs(now)

visited = [False] * (n + 1)
graph = [[] for _ in range(n + 1)]
answer = [0] * (n + 1)

for _ in range(n - 1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

dfs(1)

for i in range(2, n + 1):
    print(answer[i])