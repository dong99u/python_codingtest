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
    inst, a, b = map(int, input().split())

    if inst == 0:
        union(a, b)
    elif inst == 1:
        if find(a) == find(b):
            print('YES')
        else:
            print('NO')