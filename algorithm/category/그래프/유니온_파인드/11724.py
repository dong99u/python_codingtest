import sys
input = sys.stdin.readline

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(x, y):
    x = find(x)
    y = find(y)

    if x == y:
        return

    parent[y] = x

n, m = map(int, input().split())
parent = [i for i in range(n + 1)]

for _ in range(m):
    x, y = map(int, input().split())
    union(x, y)

answer = len(set([find(i) for i in range(1, n + 1)]))

print(answer)