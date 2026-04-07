import sys
input = sys.stdin.readline

INF = float('inf')

n, m = map(int, input().split())

graph = [[] for _ in range(n + 1)]
dist = [INF] * (n + 1)
dist[0] = None
dist[1] = 0

for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))

for _ in range(n - 1):
    for u in range(1, n + 1):
        for v, w in graph[u]:
            if dist[v] > dist[u] + w:
                dist[v] = dist[u] + w

cycle_exist = False

for u in range(1, n + 1):
    for v, w in graph[u]:
        if dist[v] > dist[u] + w:
            cycle_exist = True

if cycle_exist:
    print(-1)
else:
    for i in range(2, n + 1):
        if dist[i] != INF:
            print(dist[i])
        else:
            print(-1)
