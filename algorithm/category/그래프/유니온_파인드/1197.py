import sys
input = sys.stdin.readline
sys.setrecursionlimit(10000000)

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
    a, b, c = map(int, input().split())
    edges.append((a, b, c))

edges.sort(key=lambda x: x[2])

answer = 0
for s, e, w in edges:
    if find(s) == find(e):
        continue

    union(s, e)
    answer += w

print(answer)