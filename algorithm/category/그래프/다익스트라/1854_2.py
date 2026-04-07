import heapq, sys
from bisect import insort
input = sys.stdin.readline

n, m, k = map(int, input().split())
graph = [[] for _ in range(n + 1)]
distance = [[] for _ in range(n + 1)]

for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))

h = [(0, 1)]

while h:
    dist, now = heapq.heappop(h)

    # 현재 노드에 k개 미만이면 추가
    if len(distance[now]) < k:
        insort(distance[now], dist)

        # 인접 노드 탐색
        for next, cost in graph[now]:
            new_cost = dist + cost
            heapq.heappush(h, (new_cost, next))

for i in range(1, n + 1):
    if len(distance[i]) < k:
        print(-1)
    else:
        print(distance[i][k - 1])