import heapq
import sys
input = sys.stdin.readline

INF = float('inf')
n, m, k = map(int, input().split())
graph = [[] for _ in range(n + 1)]

dist = [[] for _ in range(n + 1)]

for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))

heap = [(0, 1)]

while heap:
    cost, now = heapq.heappop(heap)

    if len(dist[now]) < k:
        heapq.heappush(dist[now], -cost)
    elif cost < -dist[now][0]:
        heapq.heappop(dist[now])
        heapq.heappush(heap, dist[now], -cost)
    else:
        continue

    for next, c in graph[now]:
        new_dist = cost + c

        if len(dist[next]) < k:
            heapq.heappush(heap, (new_dist, next))
        elif new_dist < -dist[next][0]:
            heapq.heappush(heap, (new_dist, next))

for i in range(1, n + 1):
    if len(dist[i]) < k:
        print(-1)
    else:
        print(-dist[i][0])

