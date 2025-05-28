def find(parent, x):
    if parent[x] == x:
        return parent[x]
    parent[x] = find(parent, x)
    return parent[x]

def union(parent, rank, x, y):
    a = find(parent, x)
    b = find(parent, y)

    if rank[a] < rank[b]:
        parent[a] = b
    elif rank[a] > rank[b]:
        parent[b] = a
    else:
        parent[b] = a
        rank[a] += 1


def solution(n, costs):
    costs.sort(key=lambda x: x[2])

    parent = [i for i in range(n)]

    rank = [0] * n

    min_cost = 0
    edges = 0

    for edge in costs:
        if edges == n - 1:
            break

        x = find(parent, edge[0])
        y = find(parent, edge[1])

        if x != y:
            union(parent, rank, x, y)
            min_cost += edge[2]
            edges += 1

    return min_cost