def solution(k, operations):
    parent = [i for i in range(k)] # 각 노드의 부모노드는 자기 자신
    def find(x):
        if parent[x] != x:
            parent[x] = find(parent[x])
        return parent[x]

    def union(x, y):
        a = find(x)
        b = find(y)

        if a < b: # 루트 노드가 다르면 다른 집합
            parent[b] = a
        else:
            parent[a] = b

    for operation in operations:
        if operation[0] == 'f':
            root = find(operation[1])
        elif operation[0] == 'u':
            root = union(operation[1], operation[2])

    return len(set(find(i) for i in parent))



if __name__ == '__main__':
    print(solution(3, [['u', 0, 1], ['u', 1, 2], ['f', 2]]))
    print(solution(4, [['u', 0, 1], ['u', 2, 3], ['f', 0]]))