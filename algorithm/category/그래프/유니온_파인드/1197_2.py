import sys
input = sys.stdin.readline

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(x, y):
    x = find(x)
    y = find(y)

    if x != y:
        parent[y] = x

v, e = map(int, input().split())
edges = []
parent = [i for i in range(v + 1)]
for _ in range(e):
    u, v, w = map(int, input().split())
    edges.append((u, v, w))

edges.sort(key=lambda x: x[2])

answer = 0
for u, v, w in edges:
    if find(u) == find(v):
        continue
    union(u, v)
    answer += w

print(answer)
