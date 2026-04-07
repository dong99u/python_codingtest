n, m = map(int, input().split())

graph = [[] * (n + 1) for _ in range(n + 1)]

for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))

INF = float('inf')
dist = [INF] * (n + 1)
dist[1] = 0

for _ in range(n - 1):
    for u in range(1, n + 1):
        for v, w in graph[u]:
            if dist[u] + w < dist[v]:
                dist[v] = dist[u] + w

cycle = False

for u in range(1, n + 1):
    for v, w in graph[u]:
        if dist[u] + w < dist[v]:
            dist[v] = dist[u] + w
            cycle = True

if cycle:
    print(-1)
else:
    for i in range(2, n + 1):
        if dist[i] == INF:
            print(-1)
        else:
            print(dist[i])