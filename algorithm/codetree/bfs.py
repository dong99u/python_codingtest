from collections import deque

graph = [[] for _ in range(13 + 1)]

edges = [
    (1, 3),
    (1, 4),
    (2, 1),
    (2, 6),
    (3, 2),
    (4, 3),
    (4, 7),
    (5, 3),
    (5, 4),
    (5, 9),
    (6, 8),
    (7, 5),
    (8, 5),
    (8, 11),
    (9, 8),
    (9, 10),
    (10, 12),
    (11, 13),
    (12, 13)
]

for u, v in edges:
    graph[u].append(v)

q = deque([1])

dist = [-1] * (13 + 1)
dist[1] = 0

while q:
    now = q.popleft()

    for nxt in graph[now]:
        if dist[nxt] == -1:
            dist[nxt] = dist[now] + 1

            q.append(nxt)


print(dist)


