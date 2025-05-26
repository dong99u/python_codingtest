def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[a] = b
    else:
        parent[b] = a

n, m = map(int, input().split())

parent = [i for i in range(n + 1)]

for _ in range(m):
    i, a, b = map(int, input().split())

    if i == 0: # 팀 합치기
        union(parent, a, b)
    elif i == 1: # 같은 팀 여부 확인
        if find_parent(parent, a) == find_parent(parent, b):
            print('YES')
        else:
            print('NO')