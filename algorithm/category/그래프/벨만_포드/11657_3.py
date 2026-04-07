import sys
input = sys.stdin.readline
INF = float('inf')

n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]
distance = [INF] * (n + 1)
distance[1] = 0

for _ in range(m):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))

for _ in range(n - 1):
    for now in range(1, n + 1):
        for next, cost in graph[now]:
            new_cost = distance[now] + cost

            if new_cost < distance[next]:
                distance[next] = new_cost

cycle = False

for now in range(1, n + 1):
    for next, cost in graph[now]:
        new_cost = distance[now] + cost

        if new_cost < distance[next]:
            distance[next] = new_cost
            cycle = True

if cycle:
    print(-1)
else:
    for d in distance[2:]:
        if d == INF:
            print(-1)
        else:
            print(d)