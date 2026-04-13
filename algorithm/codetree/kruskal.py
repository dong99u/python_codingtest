import sys
input = lambda: sys.stdin.readline().rstrip()

def find(x):
    if x != parent[x]:
        parent[x] = find(parent[x])
    return parent[x]

def union(x, y):
    x = find(x)
    y = find(y)

    if x == y:
        return

    if rank[x] < rank[y]:
        parent[x] = y
    elif rank[x] > rank[y]:
        parent[y] = x
    else:
        parent[y] = x
        rank[x] += 1

def kruskal(edges):
    result = 0
    edges.sort(key=lambda x: x[2])
    for u, v, w in edges:
        if find(u) != find(v):
            union(u, v)
            result += w
    return result


n, m = map(int, input().split())
edges = [tuple(map(int, input().split())) for _ in range(m)]

parent = [i for i in range(n + 1)]
rank = [0] * (n + 1)
print(kruskal(edges))
