import sys, heapq
input = sys.stdin.readline

INF = float('inf')
v, e = map(int, input().split())
k = int(input())
graph = [[] for _ in range(v + 1)]
dist = [INF] * (v + 1)
dist[k] = dist[0] = 0
visited = [False] * (v + 1)
prev = [i for i in range(v + 1)]

for _ in range(e):
    s, e, w = map(int, input().split())
    graph[s].append((e, w))

h = [(0, k)] # (dist, node)

while h:
    curr_dist, now = heapq.heappop(h)

    if visited[now]:
        continue
    visited[now] = True

    for next, weight in graph[now]:
        if not visited[next]:
            if dist[next] > curr_dist + weight:
                dist[next] = curr_dist + weight
                prev[next] = now
                heapq.heappush(h, (curr_dist + weight, next))

for i in range(1, v + 1):
    if dist[i] == INF:
        print('INF')
    else:
        print(dist[i])
