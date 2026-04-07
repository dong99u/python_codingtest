import sys
from collections import deque
input = sys.stdin.readline

n = int(input())

graph = [[] for _ in range(n + 1)]
weights = [0] * (n + 1)
D = [0] * (n + 1)

for i in range(1, n + 1):
    input_list = list(map(int, input().split()))
    weights[i] = input_list[0]

    for j in input_list[1:-1]:
        graph[j].append(i)
        D[i] += 1

q = deque()

for i in range(1, n + 1):
    if D[i] == 0:
        q.append(i)

result = [0] * (n + 1)
while q:
    now = q.popleft()
    for next in graph[now]:
        D[next] -= 1
        result[next] = max(result[next], result[now] + weights[now])
        if D[next] == 0:
            q.append(next)

for i in range(1, n + 1):
    print(result[i] + weights[i])

