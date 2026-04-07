import sys
from collections import deque
input = sys.stdin.readline

n, m, k, x = map(int, input().split())

graph = [[] for _ in range(n + 1)]
answer = []
visited = [-1] * (n + 1)

for _ in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)

q = deque()
q.append(x)
visited[x] += 1
while q:
    v = q.popleft()
    for i in graph[v]:
        if visited[i] == -1:
            visited[i] = visited[v] + 1
            q.append(i)

for i in range(n + 1):
    if visited[i] == k:
        answer.append(i)

if not answer:
    print(-1)
else:
    answer.sort()
    for i in answer:
        print(i)