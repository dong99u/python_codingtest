import sys, heapq
input = sys.stdin.readline

INF = float('inf')

n, m = map(int, input().split())
k = int(input())

graph = [[] for _ in range(n + 1)]
dist = [INF] * (n + 1)
dist[k] = 0
prev = [i for i in range(n + 1)]

for _ in range(m):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))

# 현재 노드까지의 가중치
hq = [(0, k)]

while hq:
    curr_dist, now = heapq.heappop(hq)

    for nxt, weight in graph[now]:
        if curr_dist + weight < dist[nxt]:
            dist[nxt] = curr_dist + weight
            prev[nxt] = now
            heapq.heappush(hq, (curr_dist + weight, nxt))

for i in range(1, n + 1):
    print(dist[i] if dist[i] != INF else 'INF')


