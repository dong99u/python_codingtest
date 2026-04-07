def solution(n, costs):
    def find(x):
        if parent[x] != x:
            parent[x] = find(parent[x])
        return parent[x]

    def union(x, y):
        x = find(x)
        y = find(y)

        if rank[x] < rank[y]:
            parent[x] = y
        elif rank[x] > rank[y]:
            parent[y] = x
        else:
            parent[y] = x
            rank[x] += 1

    parent = [i for i in range(n)]
    rank = [0] * n

    graph = [[] for _ in range(n)]

    costs.sort(key=lambda x: x[2])

    answer = 0
    for u, v, w in costs:
        if find(u) != find(v):
            union(u, v)
            answer += w

    return answer

if __name__ == '__main__':
    print(solution(4, [[0,1,1],[0,2,2],[1,2,5],[1,3,1],[2,3,8]]))