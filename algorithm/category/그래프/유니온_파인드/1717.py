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

n, m = map(int, input().split())
parent = [i for i in range(n + 1)]

for _ in range(m):
    o, x, y = map(int, input().split())
    if o == 0:
        union(x, y)
    else:
        if find(x) == find(y):
            print('YES')
        else:
            print('NO')
