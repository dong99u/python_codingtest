import sys
from collections import deque
input = sys.stdin.readline

n = int(input())

time = [0] * (n + 1)
graph = [[] for _ in range(n + 1)]
D = [0] * (n + 1)

for i in range(n):
    insts = list(map(int, input().split()))

    for idx, inst in enumerate(insts):
        if idx == 0:
            time[i + 1] = inst
        else:
            if inst != -1:
                graph[inst].append(i + 1)
                D[i + 1] += 1

q = deque()

for i in range(1, n + 1):
    if D[i] == 0:
        q.append(i)

result = [0] * (n + 1)
while q:
    now = q.popleft()
    for next in graph[now]:
        D[next] -= 1
        result[next] = max(result[next], result[now] + time[now])
        if D[next] == 0:
            q.append(next)

for i in range(1, n + 1):
    print(result[i] + time[i])