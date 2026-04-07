def solution(k, operations):

    parent = [i for i in range(k)]
    rank = [0] * k

    def find(x):
        if parent[x] != x:
            parent[x] = find(parent[x])
        return parent[x]

    def union(x, y):
        x = find(x)
        y = find(y)

        if x == y:
            return

        if rank[x] < rank[y]:
            parent[x] = parent[y]
        elif rank[x] > rank[y]:
            parent[y] = x
        else:
            parent[y] = x
            rank[x] += 1

    for operation in operations:
        if operation[0] == 'u':
            union(operation[1], operation[2])
        else:
            find(operation[1])

    return len(set(parent))


if __name__ == '__main__':
    print(solution(3, [['u', 0, 1], ['u', 1, 2], ['f', 2]]))
    print(solution(4, [['u', 0, 1], ['u', 2, 3], ['f', 0]]))