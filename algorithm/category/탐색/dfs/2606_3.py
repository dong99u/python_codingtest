import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

def dfs(v):
    visited[v] = True
    cnt = 0
    for nxt in graph[v]:
        if not visited[nxt]:
            cnt += 1          # nxt가 새로 감염됨
            cnt += dfs(nxt)   # nxt로부터 퍼지는 감염 수
    return cnt

n = int(input())
m = int(input())

graph = [[] for _ in range(n + 1)]
visited = [False] * (n + 1)

for _ in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

print(dfs(1))