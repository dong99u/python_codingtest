import heapq

def solution(N, road, K):
    INF = float('inf')
    graph = [[] for _ in range(N + 1)]

    distances = [INF] * (N + 1)
    distances[1] = 0

    for u, v, w in road:
        graph[u].append((v, w))
        graph[v].append((u, w))

    heap = []
    heapq.heappush(heap, (0, 1))
    while heap:
        dist, node = heapq.heappop(heap)

        for next_node, next_dist in graph[node]:
            cost = dist + next_dist
            if cost < distances[next_node]:
                distances[next_node] = cost
                heapq.heappush(heap, (cost, next_node))

    return sum(1 for dist in distances if dist <= K)

if __name__ == '__main__':
    print(solution(6, [[1,2,1],[1,3,2],[2,3,2],[3,4,3],[3,5,2],[3,5,3],[5,6,1]], 4))