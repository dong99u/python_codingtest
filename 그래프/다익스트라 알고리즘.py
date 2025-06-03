import sys
import heapq
INF = sys.maxsize

def solution(graph, start):
    distances = {node: INF for node in graph}

    distances[start] = 0
    q = []
    heapq.heappush(q, [distances[start], start])
    paths = {start: [start]}

    while q:
        current_distance, current_node = heapq.heappop(q)
        if distances[current_node] < current_distance:
            continue

        for adj_node, weight in graph[current_node].items():
            distance = current_distance + weight

            if distance < distances[adj_node]:
                distances[adj_node] = distance
                paths[adj_node] = paths[current_node] + [adj_node]


                heapq.heappush(q, [distance, adj_node])

    sorted_paths = {node: paths[node] for node in sorted(paths)}

    return [distances, sorted_paths]


if __name__ == '__main__':
    print(solution(
        {
            'A': {'B': 9, 'C': 3},
            'B': {'A': 5},
            'C': {'B': 1}
        },
        'A'
    ))
