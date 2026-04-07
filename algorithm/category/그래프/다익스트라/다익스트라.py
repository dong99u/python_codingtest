from collections import defaultdict
import heapq

INF = float('inf')
def solution(graph, start):
    d = defaultdict(int)
    path = defaultdict(list)

    for key in graph:
        d[key] = INF

    path[start] = [start]

    d[start] = 0

    heap = []

    heapq.heappush(heap, (0, start))

    while heap:
        weight, now = heapq.heappop(heap)
        for next in graph[now]:
            if d[next] > graph[now][next] + weight:
                d[next] = graph[now][next] + weight
                path[next] = path[now] + [next]
                heapq.heappush(heap, (d[next], next))

    return [d, path]

if __name__ == '__main__':
    print(solution(
        {
            'A': {'B': 9, 'C': 3},
            'B': {'A': 5},
            'C': {'B': 1}
        },
        'A'
    ))