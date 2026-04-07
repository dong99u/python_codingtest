import sys
import heapq
input = sys.stdin.readline

INF = float('inf')

V, E = map(int, input().split())
K = int(input())

graph = [[] for _ in range(V + 1)]
visited = [False] * (V + 1)
D = [INF] * (V + 1)
D[K] = D[0] = 0
heap = []
heapq.heappush(heap, (0, K))

for _ in range(E):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))

while heap:
    weight, now = heapq.heappop(heap)

    for next, w in graph[now]:
        if D[next] > D[now] + w:
            D[next] = D[now] + w
            heapq.heappush(heap, (D[next], next))

for i in range(1, V + 1):
    if D[i] == INF:
        print('INF')
    else:
        print(D[i])